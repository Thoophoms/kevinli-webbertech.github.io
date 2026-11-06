# MySQL Driver Troubleshooting

When you are coding Python with Mysql, you would often have driver issue.

The issue lies in where you installed your driver, and which pip or python you are using, sometimes you might have a few different versions python installed or even from anaconda.

1. Recommended way

Use Python virtual environment. This solution is skipped in here.

In this article we will talk about using pyCharm to solve this driver issue,

When you try to address the issue, copy the following code to your IDE and then run it,

The following code shows the above result,

```
import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mysql')
mycursor = mydb.cursor()

mycursor.execute("select * from user")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mydb.close()
```

Ideally, you will see the following screenshot,

![alt text](https://kevinli-webbertech.github.io/blog/images/database/pyCharm.png)

* Make sure you create a Python virtual environment.
* If not, then you are likely to see the following issue **"module not found"** issue, you will  need to uninstall two packages,

`pip uninstall mysql-connector`

`pip install mysql-connector`

and 

`pip uninstall mysql-connector-python`

`pip install mysql-connector-python`

**Restart your pyCharm**

**Rerun the above code** 

Here is MySQL version:

```
mysql  Ver 8.0.36-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))
 
Python 3.10.12
```