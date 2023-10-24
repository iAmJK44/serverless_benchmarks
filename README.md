# Extreme Data Serverless Benchmarks

This repository contains a summary of serverless benchmarks and pipelines designed to measure the performance of serverless architectures like Lithops.

| Benchmark   | Description     |     Data set     |     Data format     |
|:--------|:--------|:--------:|:--------:|
| **General**  ||     
|    [*FLOPS Computation Test*](#1-flops-computation-test)      |      Analyze Lithops computation in FLOPS.     |    Autogenerated    |    NumPy array    |
|    [*Object Storage Test*](#2-object-storage-test)      |      Measure the bandwidth from FaaS Service.     |    Autogenerated    |    Bytes    |
|     [*Montecarlo*](#3-montecarlo-simulations)     |     Monte Carlo Methods to make computations with big amount of random data.     |      Autogenerated    |    NumPy array    |
|     [*Hyperparameter tunning*](#4-hyperparameter-tunning-with-grid-search)     |     Hyperparameter tuning using grid search algorithm.     |    [Amazon customer reviews](https://www.kaggle.com/bittlingmayer/amazonreviews)      |     ft.txt     |
|     **Geospatial**     |          |          |          |
|     [*NDVI*](#5-ndvi-calculation)     |     Calculate NDVI from Object Storage images.     |   Sentinel2 satellite image from the [AWS Sentinel2 open data repository](https://registry.opendata.aws/sentinel-2/)      |        Cloud-Optimized GeoTIFF (COG)  |
|     [*Model creation from LiDAR pre-processing*](#6-model-creation-from-lidar-pre-processing)     |     Create terrain models using LiDAR partitioner.     |     [laz files](https://www.icgc.cat/es/Descargas/Elevaciones/Datos-lidar)     |     laz     |
|     **Metabolomics**     |          |          |          |
|     [*METASPACE metabolite annotation*](#7-metaspace-metabolite-annotation-pipeline)     |      Run the METASPACE metabolite annotation pipeline on cloud resources.     |     [Examples of datasets and databases](https://github.com/metaspace2020/Lithops-METASPACE#example-datasets)     |     imzML     |
|      **Genomics**    |          |          |          |
|      [*Variant Calling*](#8-variant-calling)    |    Alignment of sequencing reads, stored as FASTQ files, to a reference genome, stored as a FASTA file.      |  Trypanosome [[Genome](https://tritrypdb.org/tritrypdb/app/downloads/Current_Release/TbruceiTREU927/fasta/data/), [SRR6052133](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR6052133&display=download)], Human [[Genome](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/bigZips/), [SRR15068323](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR15068323&display=data-access) , [ERR9856489](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=ERR9856489&display=data-access)], Bos Taurus [[Genome](https://www.ensembl.org/Bos_taurus/Info/Index), [SRR934415](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR934415&display=data-access)]  |     fast, fastq     |
|     **Astronomics**     |          |          |          |
|     [*Astronomica-interferometry*](#9-astronomica-interferometry)    |     Radio interferometric data processing.     |  [SB205.MS SB206.MS SB207.MS SB208.MS SB209.MS SB210.MS](https://share.obspm.fr/s/ezBfciEfmSs7Tqd?path=%2FDATA)        |  MS    |
|      **Elastic Exploration**    |          |          |          |
|     [*UTS*](#10-uts)    |    The Unbalanced Tree Search (UTS) benchmark.     |      Autogenerated    |  Dynamic tree  |
|     [*Mandelbrot with Mariani Silver*](#11-mandelbrot-with-mariani-silver)    |  Render the Mandelbrot set using  Marian-Silver algorithm.    |    Autogenerated    |  Mandelbrot set  |
|     [*Betweenness Centrality*](#12-betweenness-centrality)    |    Compute the Between Centrality (BC) algorithm.      |    Autogenerated     |  Graph  |
|  **Extreme Sorting**  |          |          |          |
| [*TeraSort*](#13-terasort)    |   Implementation of the TeraSort benchmark built on Lithops.     |    [TeraGen](https://github.com/gfinol/teragen-lithops)    |  ascii  |


In most cases there's a link to an external repository containing the code while others can be found here.

All workflows except the ones in **Elastic Exploration** utilize **[Lithops](https://lithops.cloud)** to easily deploy and run code on any major Cloud serverless platform.

# Benchmarks

For the geospatial benchmarks you first need to follow this [instructions](https://github.com/cloudbutton/geospatial-usecase/blob/main/INSTALL.md) to set up the environment. Find more information about Geospatial, Genomics and Metabolomics benchmarks [here](https://cloudbutton.eu/docs/deliverables/CloudButton_D2.5.pdf).

## 1. [FLOPS Computation Test](https://github.com/lithops-cloud/applications/tree/master/benchmarks/flops)

This is a benchmark to estimate the floating-point performance of the system for matrix multiplication operations using NumPy. It measures how many floating-point operations per second the system can perform for this specific operation.

## 2. [Object Storage Test](https://github.com/lithops-cloud/applications/tree/master/benchmarks/object_storage)

This benchmark measures the bandwidth using data transfer in Object Storage with a FaaS Service.

## 3. [Montecarlo Simulations](https://github.com/lithops-cloud/applications/tree/master/montecarlo)

This contains two applications in which Monte Carlo Methods is used to make computations with big amount of random data using Cloud Functions with Lithops. 

## 4. [Hyperparameter Tunning with Grid Search](https://github.com/lithops-cloud/applications/tree/master/sklearn)

Perform hyperparameter tuning using grid search algorithm. We have a dataset consisting of amazon product reviews and a sklearn classifier to classiy these reviews. We take advantage of cloud functions to tune this classifier's hyperparameters and show how Lithops can be used for this kind of computations.

## 5. [NDVI Calculation](https://github.com/cloudbutton/geospatial-usecase/tree/main/ndvi-diff)

Use case of serverless image processing consuming data from Object Storage, NDVI(Normalized Difference Vegetation Index) is calculated over many images to demonstrate high throughput and performance.

## 6. [Model creation](https://github.com/cloudbutton/geospatial-usecase/tree/main/calculate-models) from [LiDAR pre-processing](https://github.com/cloudbutton/geospatial-usecase/tree/main/lidar-partitioner)
LIDAR is a novel tool to partition LiDAR files based on the denisty of points. The partitions are simmilar in size, which is convenient for serverless processing, as task granularity defines the execution time and cost. With this partitioned data we create several terrain models used in many geospatial workflows. We study the impact of load balancing by partitioning LiDAR data using the aforementioned density-based partitioner.

## 7. [METASPACE metabolite annotation pipeline](Lithops-METASPACE/)

Demonstrate using Lithops to run the METASPACE (Spatial metabolomics cloud platform that conducts molecular annotation of imaging mass spectrometry data) metabolite annotation pipeline on cloud resources. 

The original implementation of this pipeline can be found on [Metaspace repository](https://github.com/metaspace2020/Lithops-METASPACE). We have addapted this implementation to work with Lithops 3.0.1 and with more recent package versions.

More information about this pipeline can be found on this [IBM Blog post](https://www.ibm.com/blog/decoding-dark-molecular-matter-in-spatial-metabolomics-with-ibm-cloud-functions/)

## 8. [Variant Calling](https://github.com/CLOUDLAB-URV/serverless-genomics/tree/main)

In genomics, variant calling entails the alignment process, which is essentially a search for string similarities. This process aligns sequencing reads, typically stored as FASTQ files, with a reference genome, which is stored as a FASTA file. The reference genome and reads are split into smaller chunks for alignment.

## 9. [Astronomica Interferometry](serverlessextract/)

Processing radio interferometric data performing all the phases: rebinning, calibration and imaging using Lithops. 

## 10. [UTS](https://github.com/gfinol/elastic-exploration)

The implementation of UTS presented here is the first that tackles an elastic resource provisioning.

## 11. [Mandelbrot with Mariani Silver](https://github.com/gfinol/elastic-exploration)

Render the Mandelbrot set using the Marian-Silver algorithm as optimization technique. This algorithm relies on the fact that the Mandelbrot250
set is connected: there is a path between any two points belonging to the set

## 12. [Betweenness Centrality](https://github.com/gfinol/elastic-exploration)

Computing the Between Centrality (BC) algorithm. The implementation follows the Brandes’ algorithm described in the benchmark, augmenting Dijkstra’s single-
source shortest paths (SSSP) algorithm for unweighted graphs.

## 13. [TeraSort](https://github.com/GEizaguirre/terasort-lithops)

Implementation of the TeraSort benchmark (a distributed sort), built on Lithops. Tasks are executed on cloud functions, object storage is used for reading & writing data (including the exchange of itnermediate files).
More information about this pipeline can be found on the following links:
   - [Paper 1](https://dl.acm.org/doi/10.1145/3429357.3430522)
   - [Paper 2](https://dl.acm.org/doi/abs/10.1145/3528535.3565241)

