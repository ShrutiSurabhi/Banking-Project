# Guided Capstone Step Five - Pipeline Orchestration <br>

There are many ways to define a workflow and it’s scope, but typically workflows are repeatable
pipeline units which can be run independently. In cloud architecture, a workflow can be run in an
elastic Hadoop cluster with input and output data that are persistent on cloud storage such as
Azure Blob Storage. The guided pipeline can be divided into two workflows: <br>
- Preprocessing Workflow: data ingestion and batch load <br>
- Analytical Workflow: analytical ETL job <br>


In this project, we launched the Spark job using a command line shell script in each workflow.
# Learning Objectives: <br>
The process has following steps: <br>
● Write shell script to submit Spark jobs <br>
● Execute Spark jobs in Azure Elastic Clusters <br>
● Design job status tracker <br>

# Prerequisites: <br>
- Azure Elastic Cluster <br>
- Knowledge of command line <br>
- 
# Summary
In this step, we practised a basic end-to-end operation on the pipeline you built. Shell scripts
are usually the most straightforward, reliable way to trigger a job. You implemented job status
tracking, which gives you the ability to monitor the progress of the daily job run, in order to make
sure that results are always delivered.
