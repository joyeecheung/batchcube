# Batch Cube
  Python Implementation of Batch Data Cube on MapReduce.

# How to run

E.g. on hadoop 1.0.4:

```
$ hadoop fs -mkdir [HDFS DIR FOR INPUT]
$ hadoop fs -copyFromLocal [PATH TO LOCAL FILE(S)] [HDFS DIR FOR INPUT]
$ hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-mapper mapper.py   -file mapper.py\
-reducer reducer.py  -file reducer.py \
-input [HDFS DIR FOR INPUT]/* -output [HDFS DIR FOR OUTPUT]
```

# Data Format

Format of input should be consistent with [1].

## Sample input (headers are ommited in actual input)
| rid | uid | country | state | city | topic | category | product | sales|
|-----|-----|---------|-------|------|-------|----------|---------|------|
| 1 | 400141 | 3 | 78 | 3427 | 3 | 59 | 4967 | 4670.08 |
| 2 | 783984 | 1 | 34 | 9 | 1 | 5 | 982 | 5340.9 |
| 3 | 4945 | 1 | 47 | 1658 | 1 | 7 | 363 | 3065.37 |
| 4 | 468352 | 2 | 57 | 2410 | 2 | 37 | 3688 | 9561.13 |

## Sample output (headers are ommited in actual output)
| indexes | values | measure |
|---------|--------|---------|
| 2 3 4   | 3 23 1132 | 10  |
| 2 3     | 3 23      | 132 |
| 2       | 3         | 992 |

# Reference
[1] Arnab Nandi, Cong Yu, Philip Bohannon, and Raghu Ramakrishnan. Data cube materialization and mining over mapreduce. *IEEE Transactions on Knowledge and Data Engineering*, 24(10):1747–1759, 2012.
