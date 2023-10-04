# Lithops Serverless Benchmarks

This repository contains a summary of serverless benchmarks and pipelines designed to measure the performance of serverless architectures like Lithops.

| Benchmark   | Description     |     Data set     |     Data size     |
|:--------|:--------|:--------:|:--------:|
| **General**  ||     
|    [*Lithops Benchmarks*](#1-lithops-compute-and-storage-benchmarks)      |      Analyze Lithops compute and storage performance.     |    Autogenerated    |        |
|     [*Montecarlo*](#2-montecarlo-simulations)     |     Monte Carlo Methods to make computations with big amount of random data.     |      Autogenerated    |          |
|     [*Hyperparameter tunning*](#3-hyperparameter-tunning-with-grid-search)     |     Hyperparameter tuning using grid search algorithm.     |    Amazon customer reviews ([link](https://www.kaggle.com/bittlingmayer/amazonreviews))      |     516.93 MB     |
|     **Geospatial**     |          |          |          |
|     [*NDVI*](#4-ndvi-calculation)     |     Calculate NDVI from Object Storage images.     |   Sentinel2 satellite image from the [AWS Sentinel2 open data repository](https://registry.opendata.aws/sentinel-2/)      |          |
|     [*Model creation from LiDAR pre-processing*](#5-model-creation-from-lidar-preprocessing)     |     Create terrain models using LiDAR partitioner.     |     [laz files](https://www.icgc.cat/es/Descargas/Elevaciones/Datos-lidar)     |     431 MB     |
|     **Metabolomics**     |          |          |          |
|     [*METASPACE*](#6-metaspace)     |      Run the METASPACE metabolite annotation pipeline on cloud resources.     |     Examples of datasets and databases in the link below     |          |
|      **Genomics**    |          |          |          |
|      [*Variant Calling*](#7-variant-calling)    |    Alignment of sequencing reads, stored as FASTQ files, to a reference genome, stored as a FASTA file.      |  Trypanosome, Human, Bos Taurus (see links below)  |     703 MB, 14.184 GB, 17.263 GB     |
|     **Astronomics**     |          |          |          |
|     [*Astronomica-interferometry*](#8-astronomica-interferometry)    |     Radio interferometric data processing.     |  [SB205.MS SB206.MS SB207.MS SB208.MS SB209.MS SB210.MS](https://share.obspm.fr/s/ezBfciEfmSs7Tqd?path=%2FDATA)        |  5.5 GB each sample    |


In most cases there's a link to an external repository containing the code while others can be found here.

All workflows utilize [Lithops](https://lithops.cloud) to easily deploy and run code on any major Cloud serverless platform.

# Benchmarks

For the geospatial benchmarks you first need to follow this [instructions](https://github.com/cloudbutton/geospatial-usecase/blob/main/INSTALL.md) to set up the environment.

## 1. [Lithops Compute and Storage Benchmarks](https://github.com/lithops-cloud/applications/tree/master/benchmarks)

This is a benchmark to estimate the floating-point performance of the system for matrix multiplication operations using NumPy. It measures how many floating-point operations per second the system can perform for this specific operation.

## 2. [Montecarlo Simulations](https://github.com/lithops-cloud/applications/tree/master/montecarlo)

This contains two applications in which Monte Carlo Methods is used to make computations with big amount of random data using Cloud Functions with Lithops. 

## 3. [Hyperparameter Tunning with Grid Search](https://github.com/lithops-cloud/applications/tree/master/sklearn)

Pre-processing of Sentinel2 images to enable serverless massive parallel processing with many workers consuming data from Object Storage using the Cloud-Optimized GeoTIFF format.

## 4. [NDVI Calculation](https://github.com/cloudbutton/geospatial-usecase/tree/main/ndvi-diff)

Use case of serverless image processing consuming data from Object Storage, NDVI(Normalized Difference Vegetation Index) is calculated over many images to demonstrate high throughput and performance.

## 5. [Model creation](https://github.com/cloudbutton/geospatial-usecase/tree/main/calculate-models) from [LiDAR pre-processing](https://github.com/cloudbutton/geospatial-usecase/tree/main/lidar-partitioner)
LIDAR is a novel tool to partition LiDAR files based on the denisty of points. The partitions are simmilar in size, which is convenient for serverless processing, as task granularity defines the execution time and cost. With this partitioned data we create several terrain models used in many geospatial workflows. We study the impact of load balancing by partitioning LiDAR data using the aforementioned density-based partitioner.

## 6. [METASPACE](https://github.com/metaspace2020/Lithops-METASPACE)

Demonstrate using Lithops to run the METASPACE (Spatial metabolomics cloud platform that conducts molecular annotation of imaging mass spectrometry data) metabolite annotation pipeline on cloud resources.

## 7. [Variant Calling](https://github.com/CLOUDLAB-URV/serverless-genomics/tree/main)

In genomics, variant calling entails the alignment process, which is essentially a search for string similarities. This process aligns sequencing reads, typically stored as FASTQ files, with a reference genome, which is stored as a FASTA file. The reference genome and reads are split into smaller chunks for alignment.

## 8. [Astronomica Interferometry](serverlessextract/)

Processing radio interferometric data performing all the phases: rebinning, calibration and imaging using Lithops. 



