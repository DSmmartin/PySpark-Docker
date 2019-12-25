# OpenJDK Version "13.0.1"
FROM maven@sha256:43e03f509bb1abfa7ea948485bef2dd5cc6f92bc72f2ed0bc0d312a4fe037bf0


ENV SPARK_VERSION=2.4.4
ENV HADOOP_VERISION=2.7
ENV SPARK_BIN=https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERISION}.tgz
ENV SPARK_FILENAME=spark-${SPARK_VERSION}.tgz
ENV WORKDIR=/home/spark

RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
RUN echo ${SPARK_BIN}}
RUN curl -o ${SPARK_FILENAME} ${SPARK_BIN} && \
    tar zxvf ${SPARK_FILENAME}

COPY pyspark-2.7.13/ /${WORKDIR}/pyspark-2.7.13
