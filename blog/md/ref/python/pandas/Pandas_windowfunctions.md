# Pandas Window Functions

Pandas provide few variants like rolling, expanding and exponentially moving weights for window statistics. 
Among these are sum, mean, median, variance, covariance, correlation, etc.

We will now learn how each of these can be applied on DataFrame objects.

## Rolling Function

The `.rolling()` function in Pandas is used to provide rolling window calculations on DataFrame objects. It computes statistics such as sum, mean, median, variance, etc., over a specified window of observations.

### Example:
```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Apply rolling window calculation for mean
rolling_mean = df['A'].rolling(window=3).mean()
print(rolling_mean)
```

## Expanding Function

The `.expanding()` function is used to provide expanding window calculations on DataFrame objects. It calculates statistics over all observations seen so far.

### Example:
```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Apply expanding window calculation for mean
expanding_mean = df['A'].expanding(min_periods=1).mean()
print(expanding_mean)
```

## Exponentially Weighted Moving Average (ewm)

The `.ewm()` function computes exponentially weighted moving averages on DataFrame objects. 
It gives more weight to recent observations while calculating the average.

### Example:
```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Apply exponentially weighted moving average
ewm_mean = df['A'].ewm(span=3).mean()
print(ewm_mean)
```

These functions are useful for generating rolling, expanding, and exponentially weighted moving statistics, providing valuable insights into time-series data.