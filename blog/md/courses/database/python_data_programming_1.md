# Python Data Programming - Database Access

## Mongo DB connection from Python

The following code will create a new document into the mongo db.

For instance, we start the mongodb from the following command,

`xiaofengli@xiaofenglx:~/code/scanhub$ sudo service mongod start`

![mongo_status.png](../../../images/database/mongo_status.png)

Type `mongosh`, the shell CLI to connect to your mongodb, then you can find the url,

```shell
xiaofengli@xiaofenglx:~/code/scanhub$ mongosh
Current Mongosh Log ID:	6747d3d7841b5c4a7a964032
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.1
Using MongoDB:		7.0.14
Using Mongosh:		2.3.1
mongosh 2.3.3 is available for download: https://www.mongodb.com/try/download/shell

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2024-11-27T21:20:19.334-05:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2024-11-27T21:20:21.087-05:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
------

```

Let us take that `mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.1` and put it into our python code in the following,

```python
import pymongo

# Connect to MongoDB

uri="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.1"
client = pymongo.MongoClient(uri)

# Access the database and collection

db = client["shop"]
collection = db["inventory"]

# Create a document to insert
new_document = {"name": "John Doe", "age": 30}

# Insert the document
result = collection.insert_one(new_document)
print(f"Inserted document with ID: {result.inserted_id}")
```

Another example,

```python
import pymongo

# Connect to MongoDB

uri="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.1"

client = pymongo.MongoClient(uri)

# Access the database and collection

db = client["shop"]

collection = db["inventory"]

# Create a document to insert

new_document = {"name": "Kevin Li", "age": 28}

# Insert the document

#result = collection.insert_one(new_document)
#print(f"Inserted document with ID: {result.inserted_id}")

collection.update_many({},{"$inc": { "age": 1 }})

searchedRecords = collection.find({})
#print(f"Find all documents in the collection： {searchedRecords}")
print(type(searchedRecords))

for document in searchedRecords:
    print(document) # iterate the cursor
```

## MySQL Connection from Python

Here’s an example of Python code to connect to a MySQL database using the `mysql-connector-python` library:

### Step 1: Install the required library
Before running the code, ensure you have the `mysql-connector-python` library installed. You can install it using pip:
```bash
pip install mysql-connector-python
```

### Step 2: Use the following Python code
```python
import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your host
            database='your_database_name',  # Replace with your database name
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            print("Successfully connected to MySQL")
            
            # Get server info
            db_info = connection.get_server_info()
            print("Server version:", db_info)
            
            # Optionally create a cursor and fetch data
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Connected to database:", record)
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function
connect_to_mysql()
```

### Explanation of the Code:
1. **Connection Parameters**: Replace `host`, `database`, `user`, and `password` with your actual database connection details.
2. **Check Connection**: `connection.is_connected()` verifies if the connection is successful.
3. **Cursor Operations**: A `cursor` is used to execute SQL commands.
4. **Error Handling**: Errors during connection are caught using a `try-except` block.
5. **Close Resources**: Ensure the connection is closed in the `finally` block to free up resources.

### Example Output
```
Successfully connected to MySQL
Server version: 8.0.27
Connected to database: ('your_database_name',)
MySQL connection is closed
```

Let me know if you need help with specific queries or handling advanced scenarios!

[MySQL Example](https://kevinli-webbertech.github.io/blog/html/ref/database/mysql_driver.html)


## SQLite Connection from Python

Connecting to an SQLite database in Python is straightforward because Python comes with built-in support for SQLite via the `sqlite3` module.

Here’s an example of Python code to connect to an SQLite database:

### Python Code for SQLite Connection
```python
import sqlite3

def connect_to_sqlite():
    try:
        # Connect to SQLite database
        # If the database does not exist, it will be created
        connection = sqlite3.connect("example.db")  # Replace 'example.db' with your database name
        print("Successfully connected to SQLite")

        # Create a cursor object
        cursor = connection.cursor()

        # Example query to check the SQLite version
        cursor.execute("SELECT sqlite_version();")
        record = cursor.fetchone()
        print("SQLite version:", record[0])

    except sqlite3.Error as e:
        print("Error while connecting to SQLite", e)
    finally:
        if 'connection' in locals():
            # Close the database connection
            connection.close()
            print("SQLite connection is closed")

# Call the function
connect_to_sqlite()
```

### Explanation of the Code:
1. **`sqlite3.connect`**: Creates a connection to an SQLite database file. If the file does not exist, SQLite creates it.
2. **Cursor Object**: `cursor` is used to execute SQL queries.
3. **SQLite Version**: The sample query retrieves the SQLite version for demonstration purposes.
4. **Error Handling**: Any errors during the connection or operations are caught with a `try-except` block.
5. **Closing the Connection**: Always close the connection after operations to free up resources.

### Example Output:
```
Successfully connected to SQLite
SQLite version: 3.39.2
SQLite connection is closed
```

### Tips:
- **Database File Path**: Use the full path if the database file is not in the current working directory.
- **In-Memory Database**: For temporary databases, use `sqlite3.connect(":memory:")`.

Let me know if you need help executing specific queries or designing an SQLite schema!