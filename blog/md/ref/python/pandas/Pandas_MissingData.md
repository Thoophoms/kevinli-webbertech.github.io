# Handling Missing Values in Pandas

Missing data is a common issue in real-life datasets, affecting the accuracy and reliability of analyses and models. Pandas provides powerful tools to handle missing values effectively. Let's explore various techniques to deal with missing data along with examples.

## When and Why Data Is Missed?

Data can be missing due to various reasons such as incomplete surveys, user omission, or technical issues. Addressing missing data is crucial to maintain data quality and ensure accurate analysis.

## Check for Missing Values

Pandas offers `isnull()` and `notnull()` functions to detect missing values.

**Example 1: Check for missing values in a column**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df['one'].isnull())
```

**Output:**

```
a    False
b     True
c    False
d     True
e    False
f    False
g     True
h    False
Name: one, dtype: bool
```

**Example 2: Check for non-null values in a column**

```python
print(df['one'].notnull())
```

**Output:**

```
a     True
b    False
c     True
d    False
e     True
f     True
g    False
h     True
Name: one, dtype: bool
```

#### Calculations with Missing Data

Pandas treats missing values appropriately in calculations:

- Missing values are treated as zero in summing data.
- If all data in a calculation are missing, the result is NaN.

**Example 1: Summing data with missing values**

```python
print(df['one'].sum())
```

**Output:**

```
1.263097333318632
```

**Example 2: Summing data with all missing values**

```python
df = pd.DataFrame(index=[0, 1, 2, 3, 4, 5], columns=['one', 'two'])
print(df['one'].sum())
```

**Output:**

```
nan
```

#### Cleaning / Filling Missing Data

Pandas provides methods to clean and fill missing values to maintain data integrity.

**Replace NaN with a Scalar Value**

**Example:**

```python
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c'])

print("Original DataFrame:")
print(df)

print("\nNaN replaced with '0':")
print(df.fillna(0))
```

**Fill NA Forward and Backward**

**Example 1: Fill missing values forward**

```python
print(df.fillna(method='pad'))
```

**Example 2: Fill missing values backward**

```python
print(df.fillna(method='backfill'))
```

#### Drop Missing Values

To exclude missing values, use the `dropna()` function.

**Example 1: Drop rows with missing values**

```python
print(df.dropna())
```

**Example 2: Drop columns with missing values**

```python
print(df.dropna(axis=1))
```

#### Replace Missing (or) Generic Values

Use the `replace()` method to replace missing or generic values.

**Example:**

```python
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})

print(df.replace({1000:10, 2000:60}))
```

These methods offer flexible ways to handle missing values in Pandas DataFrames, ensuring accurate analyses and reliable insights from your data.