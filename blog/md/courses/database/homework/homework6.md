# Homework 6 SQL Function and Groupby

Requirements:
* Provide your SQL code in word or pdf report
* Provide screenshots to make sure your code is working
* In each programming question, the above will each take 12.5 pts.

## Tasks

### Task 1

From the following tables write a SQL query to find the salesperson and customer who
reside in the same city. Return Salesman, cust_name and city. (25 pts)

***Sample table: orders***

|ord_no|    purch_amt|   ord_date|    customer_id|  salesman_id|
|-------|  ---------- | ---------- | ----------- | -----------|
|70001  |150.5  |     2012-10-05 | 3005     |    5002 |
|70009  |270.65      |2012-09-10  |3001       |  5005|
|70002  |     65.26|       2012-10-05|  3002 |        5001|
|70004  |     110.5|        2012-08-17  |3009|         5003|
|70007  |     948.5|       2012-09-10  |3005|         5002|
|70005  |     2400.6|      2012-07-27  |3007|         5001|
|70008  |     5760|        2012-09-10  |3002|         5001|
|70010  |     1983.43|     2012-10-10  |3004|         5006|
|70003  |     2480.4|      2012-10-10  |3009|         5003|
|70012  |     250.45|      2012-06-27  |3008|         5002|
|70011  |     75.29|       2012-08-17  |3003|         5007|
|70013  |     3045.6|      2012-04-25  |3002|         5001|

***Sample Output:***

```
sum
17541.18
```

### Task 2

From the following table, write a SQL query to calculate the average purchase amount of all orders. Return average purchase amount.

***Sample table: orders***

|ord_no|  purch_amt |   ord_date|    customer_id|  salesman_id|
|------|  ----------| ----------|  -----------|  -----------|
|70001|       150.5 | 2012-10-05|  3005 |       5002|
|70009|       270.65| 2012-09-10|  3001 |       5005|
|70002|       65.26 | 2012-10-05|  3002 |       5001|
|70004|       110.5 | 2012-08-17|  3009 |       5003|
|70007|       948.5 | 2012-09-10|  3005 |        5002|
|70005|       2400.6| 2012-07-27|  3007 |        5001|
|70008|       5760  | 2012-09-10|  3002 |        5001|
|70010|      1983.43| 2012-10-10|  3004 |        5006|
|70003|       2480.4| 2012-10-10|  3009 |        5003|
|70012|       250.45| 2012-06-27|  3008 |        5002|
|70011|        75.29| 2012-08-17|  3003 |        5007|
|70013|       3045.6| 2012-04-25|  3002 |        5001|

***Sample Output:***

```
avg
1461.7650000000000000
```

### Task 3

From the following table, write a SQL query that counts the number of unique salespeople. Return number of salespeople.  

***Sample table: orders***

|ord_no  |   purch_amt|   ord_date|   customer_id|  salesman_id|
|--------|  ----------| ----------|  ----------- | -----------|
|70001   |    150.5   | 2012-10-05|  3005        | 5002      |
|70009   |    270.65  | 2012-09-10|  3001        | 5005|
|70002   |    65.26   | 2012-10-05|  3002        | 5001|
|70004   |    110.5   | 2012-08-17|  3009        | 5003|
|70007   |    948.5   | 2012-09-10|  3005        | 5002|
|70005   |    2400.6  | 2012-07-27|  3007        | 5001|
|70008   |    5760    | 2012-09-10|  3002        | 5001|
|70010   |    1983.43 | 2012-10-10|  3004        | 5006|
|70003   |    2480.4  | 2012-10-10|  3009        | 5003|
|70012   |    250.45  | 2012-06-27|  3008        | 5002|
|70011   |    75.29   | 2012-08-17|  3003        | 5007|
|70013   |    3045.6  | 2012-04-25|  3002        | 5001|

***Sample Output:***

```
count
6
```

### Task 4

From the following table, write a SQL query to count the number of customers. Return number of customers.  

***Sample table: customer***

| customer_id |   cust_name    |    city    | grade | salesman_id|
|-------------|----------------|------------|-------|------------|
|        3002 | Nick Rimando   | New York   |   100 |        5001|
|        3007 | Brad Davis     | New York   |   200 |        5001|
|        3005 | Graham Zusi    | California |   200 |        5002|
|        3008 | Julian Green   | London     |   300 |        5002|
|        3004 | Fabian Johnson | Paris      |   300 |        5006|
|        3009 | Geoff Cameron  | Berlin     |   100 |        5003|
|        3003 | Jozy Altidor   | Moscow     |   200 |        5007|
|        3001 | Brad Guzan     | London     |       |        5005|

***Sample Output:***
```
count
8
```