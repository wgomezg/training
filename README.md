# training

Extract specific information from a dataset composed by proxy log files. 

Load the dataset into the HDFS at a destination folder of your choosing.
Write one MapReduce program, and Pig Scripts to:
Process proxy logs and generate the following metrics:
Top 10 most visited sites outside of Globant.com
Average response time for each site
Average bytes (data delivered to the client) for each site
The final solution should allow the user to change the bytes field in each record to a different order of magnitude (KB, MB, etc). In Pig you'll need to write a User Defined Function (UDF) which will transform the bytes field to the output magnitude specified via constructor.
Store the results into an output file in HDFS.

