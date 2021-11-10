# Airflow Mini-Project
# DAG Scheduling

In this project, we use Apache Airflow to create a data pipeline to extract online stock market
data and deliver analytical results. You’ll use Yahoo Finance as the data source. Yahoo Finance
provides intra-day market price details down a one-minute interval.
You’ll work with two stock symbols: AAPL and TSLA. The workflow should be scheduled to run
at 6 PM on every weekday (Mon - Fri), which functions as below: <br>
- Download the daily price data with one minute interval for the two symbols. Each symbol
will have a separate task, Task1 (t1) and Task2 (t2), which run independently and in
parallel. <br>
- Save both datasets into CSV files and load them into HDFS. Each symbol will have a
separate task, Task3 (t3) and Task4 (t4), which run independently and in parallel. <br>
- Run your custom query on the downloaded dataset for both symbols, Task5 (t5). Before
this step executes, all previous tasks must complete. <br>
- Use Celery Executor in Airflow to run the job. <br> 


# Learning Objectives
With this mini-project, you will utilize Apache Airflow to orchestrate your pipeline, exercise the
DAG creation, uses of various operators (BashOperator, PythonOperator, etc), setting up order
of operation of each task.
In this mini-project, you will gain familiarity with how to use Apache Airflow to automate data
pipelining tasks. Along the way, you will learn how to: <br>
● Use Apache Airflow to orchestrate your pipeline <br>
● Exercise DAG creation <br>
● Use Various Airflow operators like BashOperator and PythonOperator <br>
● Set up the order operation of each task <br>
● Use Celery Executor to run your job <br>
# Prerequisites
- Install Airflow <br>
- For this project, you’ll need Yahoo Finance’s Python library. You can install it using the
command: pip install yfinance <br>
- Install pandas using the command: pip install pandas <br>
