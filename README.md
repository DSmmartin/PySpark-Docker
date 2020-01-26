# PySpark-Docker

PySpark Docker are a set of ready-to-run Docker images containing [Spark](https://spark.apache.org) application integrated with Python and tools for developing [PySpark](https://spark.apache.org/docs/latest/api/python/index.html#)  applications.

## Requirements

1. [Docker](https://www.docker.com).

## 1. Building the Docker image

To build the Docker image run the following command:

```bash
docker build ./ -f ./base/Dockerfile -t pyspark-base
```

## 2. Launch an PySpark app

To submit your python file you have to use the *spark-submit* command.
For example the pyspark-2.7.13 example give run the following command:

```bash
docker run -it pyspark-base /spark-2.4.4-bin-hadoop2.7/bin/spark-submit ./pyspark-2.7.13/example.py
```
