import pandas as pd
import numpy as np

print("Task 1: Create a DataFrame with numpy random values (4 features and 4 observations)")
data = np.random.randn(4, 4)
df = pd.DataFrame(data)
print(df)

print("Task 2: Rename the DataFrame columns")
df.columns = ['Random value 1', 'Random value 2', 'Random value 3', 'Random value 4']
print(df)

print("Task 3: Find descriptive statistics")
print(df.describe())

print("Task 4: Check for null values and data types")
null_values = df.isnull().sum()
data_types = df.dtypes
print("Null Values:")
print(null_values)
print("Data Types:")
print(data_types)

print("Task 5: Display columns")
#Location method
x2 = df['Random value 2']
x3 = df['Random value 3']
print(x2,x3)

#Index location method
x2new = df.iloc[:, 1]
x3new = df.iloc[:, 2]
print(x2new, x3new)

