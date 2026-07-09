import pandas as pd

print("Pandas Version:", pd.__version__)

# Creating a Series
numbers = pd.Series([10, 20, 30, 40, 50])
print("Series:")
print(numbers)

# Creating a DataFrame
students = {
    "Name": ["Divya", "Aman", "Priya"],
    "Age": [21, 22, 20],
    "Marks": [92, 85, 90]
}

df = pd.DataFrame(students)

print("\nDataFrame:")
print(df)
