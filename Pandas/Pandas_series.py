import pandas as pd

# Creating a Series
marks = pd.Series([85, 92, 78, 90])

print("Student Marks:")
print(marks)

print("\nFirst Element:")
print(marks[0])

# Creating a Series with custom index
students = pd.Series(
    [85, 92, 78],
    index=["Aman", "Divya", "Priya"]
)

print("\nSeries with Custom Index:")
print(students)

print("\nMarks of Divya:")
print(students["Divya"])
