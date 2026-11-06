# Homework 2 Data Analysis with Pandas

## Problem Description

Instructions. Please write code with Pandas DataFrame to complete the following tasks.

* Task 0 (0 pt). Load the nyc taxi dataset by using the command

```python
path = ’dbfs:/databricks-datasets/nyctaxi/tripdata/green/green_tripdata_2019-12.csv.gz’
df = (
spark.read.format(’csv’)
.load(path, header=True)
.toPandas()
)
```

> The data was put in the discussion forum in canvas now.

* Task 1 (15 pts). Convert lpep pickup datetime and lpep dropoff datetime
to the type of datetime.

* Task 2 (15 pts). This dataset should only include taxi trips in December
2019. Filter out the trips whose pickup time is before December 1, 2019,
and the trips whose dropoff time is after December 31, 2019.

* Task 3 (15 pts). Filter out trips whose dropoff time is before pickup time.

* Task 4 (15 pts). Remove records that have negative values in any of the following columns.

--trip distance 
--fare amount
--extra
--mta tax 
--tip amount
--improvement surcharge
--total amount
--congestion surcharge

* Task 5 (15 pts). Remove records that have N/A values in VendorID and
print out the number of rows in the cleaned dataframe.

* Task 6. (10 pts). Remove lpep from the columns lpep pickup datetime
and lpep dropoff datetime.

* Task 7. (15 pts). Find the trip with the highest fare amount.

## Submission Guideline

1. Work individually.
2. Any code or code result, please write a doc report and paste screenshots to prove it is working.
3. After each task, execute the display() command to show the result.
4. Please submit a .ipynb file.
5. Submit your solution on Canvas on time. A late penalty of 10 points for each late day applies. Any late for more than three days receives zero automatically.