Post-Sale-Automobile-Report
Objective
The goal of this mini project is to use a MapReduce program to produce a report of the total number of accidents per make and year of the car.

Data
The sample data is from an automobile tracking platform that tracks the history of important incidents after the initial sale of a new vehicle. Such incidents include subsequent private sales, repairs, and accident reports. The platform provides a good reference for second-hand buyers to understand the vehicles they are interested in.

Column	Type
incident_id	INT
incident_type	STRING (I: initial sale, A: accident, R: repair)
vin_number	STRING
make	STRING (The brand of the car, only populated with incident type “I”)
model	STRING (The model of the car, only populated with incident type “I”)
year	STRING (The year of the car, only populated with incident type “I”)
incident_date	DATE (The year of the car, only populated with incident type “I”)
description	STRING
Data enrichment
The original sample dataset is quite small. To fully test the power of MapReduce in a distributed environment, a much richer dataset is always preferred. Therefore, under the data mocking module, I have developed a program to enrich the original dataset to a user-customizable number of records. To generate more data, use

cd data_mocking/scripts/
python data_mocking.py --gen_n 10000
Refer to data_mocking module to see details.

Running the job
The actual job is done in a Hadoop distributed systems. A Hortonworks Hadoop Sandbox was used to run and test the program. The sandbox is a pre-configured virtual machine that has all necessary installation completed. If Hadoop and Sandbox are not set up, simply use the bash pipeline command to simulate what happens in MapReduce. This will not work in distributed mode, but it can be used to test the functionality.
