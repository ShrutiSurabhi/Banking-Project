5.1 Preprocessing Workflow
Use a shell script to call a data ingestion Spark job:
#!/bin/sh
. ~/.bash_profile
spark-submit \
--master local \
--py-files dist/guidedcapstone-1.0-py3.7.egg \
--jars jars/postgresql-42.2.14.jar, jars/hadoop-azure.jar, jars/azure-storage.jar
\
etl/src/run_data_ingestion.py \
config/config.ini
5.2 Analytical Workflow
Use shell script to call an analytical ETL job:
#!/bin/sh
. ~/.bash_profile
spark-submit \
--master local \
--py-files dist/guidedcapstone-1.0-py3.7.egg \
--jars jars/postgresql-42.2.14.jar, jars/hadoop-azure.jar, jars/azure-storage.jar \
etl/src/run_reporter.py \
config/config.ini
5.3 Job Status Tracking
In the daily operation of a product, failures in system or application level are expected to occur
from time to time. Maintaining job status is very important in order to keep track of successful
and failed job runs, so you can then take proper actions.
Typical job status is maintained in a database table which supports transactional operations like
insert, update, delete, etc.
5.3.1 Defining A Job Status Table
An entry to your job status table should uniquely identify the actual job which runs on a certain
date, since all of your jobs run only once per day.
Your job status table should contain these fields:
- Job_id (primary and unique): naming convention can be jobname_yyyy-mm-dd
- Status: success or failure state of the job
- Updated_time: datetime of the entry
