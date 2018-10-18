#!/bin/bash


NUM_CORES=*
DRIVER_MEM=3g

JARS="/usr/share/spark/spark-2.3.2-bin-hadoop2.7/jars/elasticsearch-hadoop-6.4.2/dist"


export SPARK_HOME="/usr/share/spark/spark-2.3.2-bin-hadoop2.7"
export PATH=$PATH:$SPARK_HOME/bin
export CODEPATH="/home/ubuntu/Documents/esearch"

cd $CODEPATH

$SPARK_HOME/bin/spark-submit --master local[$NUM_CORES] --driver-memory $DRIVER_MEM --jars $JARS/elasticsearch-hadoop-6.4.2.jar $CODEPATH/updateData.py
