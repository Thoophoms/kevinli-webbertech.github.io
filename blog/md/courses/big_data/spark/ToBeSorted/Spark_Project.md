## Step-by-Step Guide

#### 1. Setting Up the Environment

**Step 1.1: Start the Terminal**
Open your terminal (Command Prompt, PowerShell, or Terminal on macOS/Linux).

**Step 1.2: Create a Project Directory**
Navigate to your desired location and create a new directory for your project.
```sh
mkdir word_count_project
cd word_count_project
```

**Step 1.3: Download and Set Up Spark**
Download Spark if you haven't already. You can download the pre-built package from [Spark Downloads](https://spark.apache.org/downloads.html). Assuming you have it downloaded and extracted, set the `SPARK_HOME` environment variable and update the `PATH`.

```sh
export SPARK_HOME=/path/to/spark
export PATH=$SPARK_HOME/bin:$PATH
```

**Step 1.4: Initialize a PySpark Session**
Ensure you have Python installed. You can create a virtual environment to keep your dependencies isolated.

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install pyspark
```

#### 2. Creating the Word Count Program

**Step 2.1: Write the PySpark Code**
Create a new Python file for your Word Count program.

```sh
touch word_count.py
```

Open `word_count.py` in your favorite text editor and add the following code:

```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read input file
input_file = "input.txt"  # Replace with your input file path
text_file = spark.sparkContext.textFile(input_file)

# Perform word count
counts = (text_file.flatMap(lambda line: line.split(" "))
          .map(lambda word: (word, 1))
          .reduceByKey(lambda a, b: a + b))

# Collect the results and print them
output = counts.collect()
for word, count in output:
    print(f"{word}: {count}")

# Stop the Spark session
spark.stop()
```

**Step 2.2: Create an Input File**
Create an input text file named `input.txt` in the same directory with some text content.

```sh
echo "hello world hello Spark hello PySpark" > input.txt
```

**Step 2.3: Run the Code**
Run your PySpark program from the terminal.

```sh
python word_count.py
```

You should see the word counts printed to the terminal:

```
hello: 3
world: 1
Spark: 1
PySpark: 1
```

#### 3. Stopping the Spark Session

The Spark session is stopped at the end of the script with `spark.stop()`. This ensures that all resources are released properly.

```python
# Stop the Spark session
spark.stop()
```

