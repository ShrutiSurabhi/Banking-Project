# Guided Capstone Step Five - Pipeline Orchestration <br>

There are many ways to define a workflow and it’s scope, but typically workflows are repeatable
pipeline units which can be run independently. In cloud architecture, a workflow can be run in an
elastic Hadoop cluster with input and output data that are persistent on cloud storage such as
Azure Blob Storage. Your guided pipeline can be divided into two workflows: <br>
- Preprocessing Workflow: data ingestion and batch load <br>
- Analytical Workflow: analytical ETL job <br>


In this project, you’ll launch your Spark job using a command line shell script in each workflow.
# Learning Objectives: <br>
By the end of this step, you’ll: <br>
● Write shell script to submit Spark jobs <br>
● Execute Spark jobs in Azure Elastic Clusters <br>
● Design job status tracker <br>

# Prerequisites: <br>
- Azure Elastic Cluster <br>
- Knowledge of command line <br>
