register './piggybank.jar';
define SUBSTRING org.apache.pig.piggybank.evaluation.string.SUBSTRING();
define REPLACE org.apache.pig.piggybank.evaluation.string.REPLACE();
DEFINE LENGTH org.apache.pig.piggybank.evaluation.string.LENGTH();

logs = LOAD 'mapreduce/wilson.gomez/input.txt' USING PigStorage('\n') AS (line:chararray);
lineData = FOREACH logs GENERATE TRIM(SUBSTRING($0,INDEXOF($0, 'url=',4),INDEXOF($0, 'exceptions=',4))) as url,TRIM(SUBSTRING($0,INDEXOF($0, 'fullreqtime=',4),INDEXOF($0, 'device=',4))) AS time,TRIM(SUBSTRING($0,INDEXOF($0, 'size=',4),INDEXOF($0, 'request=',4))) AS size;
dump lineData;