****Post-Sale-Automobile-Report****
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
