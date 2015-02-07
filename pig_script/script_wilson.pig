register './piggybank.jar';
register './udf.py' USING streaming_python AS udf;
define SUBSTRING org.apache.pig.piggybank.evaluation.string.SUBSTRING();
define REPLACE org.apache.pig.piggybank.evaluation.string.REPLACE();
DEFINE LENGTH org.apache.pig.piggybank.evaluation.string.LENGTH();

logs = LOAD 'mapreduce/wilson.gomez/input.txt' USING PigStorage('\n') AS (line:chararray);
lineData = FOREACH logs GENERATE TRIM(SUBSTRING($0,INDEXOF($0, 'url=',4),INDEXOF($0, 'exceptions=',4))) as url,TRIM(SUBSTRING($0,INDEXOF($0, 'fullreqtime=',4),INDEXOF($0, 'device=',4))) AS time,TRIM(SUBSTRING($0,INDEXOF($0, 'size=',4),INDEXOF($0, 'request=',4))) AS size;
urlFormated = FOREACH lineData GENERATE udf.extractSite(TRIM(REPLACE(REPLACE(url,'url=',''),'"',''))) as domain, (int)TRIM(REPLACE(REPLACE(time,'fullreqtime=',''),'"','')) as reqtime, (int)TRIM(REPLACE(REPLACE(size,'size=',''),'"','')) as size;
groupUrl = GROUP urlFormated by domain;
sumarize = foreach groupUrl {
        sumreqtime = SUM(urlFormated.reqtime);
        sumsize = SUM(urlFormated.size);
	count = COUNT(urlFormated);
	sumsizeTransform = udf.transform(sumsize/count,'$parameter');
        generate FLATTEN(urlFormated.domain) as domain, count as count, sumsizeTransform as promsize, sumreqtime/count as promreqime;
};
distRes = DISTINCT sumarize;
ordRes = order distRes by count DESC;
limRes = LIMIT ordRes 10;
DUMP limRes;



