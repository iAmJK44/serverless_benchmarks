import os
import shutil
from pathlib import PurePath, _PosixFlavour
import logging
from contextlib import suppress

rebinning_param_parset = {
    "msin": "",
    "msout": "",
    "steps": "[aoflag, avg, count]",
    "aoflag.type": "aoflagger",
    "aoflag.memoryperc": 90,
    "aoflag.strategy": "/home/ayman/Downloads/pipeline/parameters/rebinning/STEP1-NenuFAR64C1S.lua",
    "avg.type": "averager",
    "avg.freqstep": 4,
    "avg.timestep": 8,
}

cal_param_parset = {
    "msin": "",
    "msin.datacolumn": "DATA",
    "msout": ".",
    "steps": "[cal]",
    "cal.type": "ddecal",
    "cal.mode": "diagonal",
    "cal.sourcedb": "/home/ayman/Downloads/pipeline/parameters/cal/STEP2A-apparent.sourcedb",
    "cal.h5parm": "",
    "cal.solint": 4,
    "cal.nchan": 4,
    "cal.maxiter": 50,
    "cal.uvlambdamin": 5,
    "cal.smoothnessconstraint": 2e6,
}

sub_param_parset = {
    "msin": "",
    "msin.datacolumn": "DATA",
    "msout": ".",
    "msout.datacolumn": "SUBTRACTED_DATA",
    "steps": "[sub]",
    "sub.type": "h5parmpredict",
    "sub.sourcedb": "/home/ayman/Downloads/pipeline/parameters/cal/STEP2A-apparent.sourcedb",
    "sub.directions": "[[CygA], [CasA]]",
    "sub.operation": "subtract",
    "sub.applycal.parmdb": "",
    "sub.applycal.steps": "[sub_apply_amp, sub_apply_phase]",
    "sub.applycal.correction": "fulljones",
    "sub.applycal.sub_apply_amp.correction": "amplitude000",
    "sub.applycal.sub_apply_phase.correction": "phase000",
}

apply_cal_param_parset = {
    "msin": "",
    "msin.datacolumn": "SUBTRACTED_DATA",
    "msout": ".",
    "msout.datacolumn": "CORRECTED_DATA",
    "steps": "[apply]",
    "apply.type": "applycal",
    "apply.steps": "[apply_amp, apply_phase]",
    "apply.apply_amp.correction": "amplitude000",
    "apply.apply_phase.correction": "phase000",
    "apply.direction": "[Main]",
    "apply.parmdb": "",
}


def delete_all_in_cwd():
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        try:
            if os.path.isfile(filename) or os.path.islink(filename):
                os.unlink(filename)
            elif os.path.isdir(filename):
                shutil.rmtree(filename)
        except Exception as e:
            print(f"Failed to delete {filename}. Reason: {e}")


class _S3Flavour(_PosixFlavour):
    is_supported = True

    def parse_parts(self, parts):
        drv, root, parsed = super().parse_parts(parts)
        for part in parsed[1:]:
            if part == "..":
                index = parsed.index(part)
                parsed.pop(index - 1)
                parsed.remove(part)
        return drv, root, parsed

    def make_uri(self, path):
        uri = super().make_uri(path)
        return uri.replace("file:///", "s3://")


class S3Path(PurePath):
    """
    PurePath subclass for AWS S3 service
    Source: https://github.com/liormizr/s3path
    S3 is not a file-system, but we can look at it like a POSIX system
    """

    _flavour = _S3Flavour()
    __slots__ = ()

    @classmethod
    def from_uri(cls, uri: str) -> "S3Path":
        """
        from_uri class method create a class instance from url

        >> from s3path import PureS3Path
        >> PureS3Path.from_url('s3://<bucket>/<key>')
        << PureS3Path('/<bucket>/<key>')
        """
        if not uri.startswith("s3://"):
            raise ValueError("Provided uri seems to be no S3 URI!")
        return cls(uri[4:])

    @classmethod
    def from_bucket_key(cls, bucket: str, key: str) -> "S3Path":
        """
        from_bucket_key class method create a class instance from bucket, key pair's

        >> from s3path import PureS3Path
        >> PureS3Path.from_bucket_key(bucket='<bucket>', key='<key>')
        << PureS3Path('/<bucket>/<key>')
        """
        bucket = cls(cls._flavour.sep, bucket)
        if len(bucket.parts) != 2:
            raise ValueError(
                "bucket argument contains more then one path element: {}".format(bucket)
            )
        key = cls(key)
        if key.is_absolute():
            key = key.relative_to("/")
        return bucket / key

    @property
    def bucket(self) -> str:
        """
        The AWS S3 Bucket name, or ''
        """
        self._absolute_path_validation()
        with suppress(ValueError):
            _, bucket, *_ = self.parts
            return bucket
        return ""

    @property
    def key(self) -> str:
        """
        The AWS S3 Key name, or ''
        """
        self._absolute_path_validation()
        key = self._flavour.sep.join(self.parts[2:])
        return key

    @property
    def virtual_directory(self) -> str:
        """
        The parent virtual directory of a key
        Example: foo/bar/baz -> foo/baz
        """
        vdir, _ = self.key.rsplit("/", 1)
        return vdir

    def as_uri(self) -> str:
        """
        Return the path as a 's3' URI.
        """
        return super().as_uri()

    def _absolute_path_validation(self):
        if not self.is_absolute():
            raise ValueError("relative path have no bucket, key specification")

    def __repr__(self) -> str:
        return "{}(bucket={},key={})".format(
            self.__class__.__name__, self.bucket, self.key
        )
