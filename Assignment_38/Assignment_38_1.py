# 1. Write a program to load the file student_performance_ml.csv using pandas.
# Display:
#     1) First 5 records
#     2) Last 5 records
#     3) Total number of rows and columns
#     4) List of column names
#     5) Data types of each column3

import pandas as  pd

Border = "-"*40

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)
print("Dataset loaded successfully...")

print("First 5 records : ")
print(df.head())

print("Last 5 records : ")
print(df.tail())

print("Total number of rows and columns:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("List of Column Names:")
print(df.columns.tolist())

print("Data Types of each column:")
print(df.dtypes)