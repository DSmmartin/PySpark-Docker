# OpenJDK Version "13.0.1"
FROM maven@sha256:43e03f509bb1abfa7ea948485bef2dd5cc6f92bc72f2ed0bc0d312a4fe037bf0


ENV SPARK_VERSION=2.4.4
ENV HADOOP_VERISION=2.7
ENV SPARK_BIN=https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERISION}.tgz
ENV SPARK_FILENAME=spark-${SPARK_VERSION}.tgz
ENV WORKDIR=/home/spark
ENV SPARK_DIR=/opt/spark

RUN curl -o opt/${SPARK_FILENAME} ${SPARK_BIN} && \
    tar zxvf opt/${SPARK_FILENAME}

RUN export SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERISION}/
RUN export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
COPY pyspark-2.7.13/ /${WORKDIR}/pyspark-2.7.13
