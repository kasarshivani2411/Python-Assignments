# 1. Write a program to load the file student_performance_ml.csv using pandas.
# Display:
#     1) First 5 records
#     2) Last 5 records
#     3) Total number of rows and columns
#     4) List of column names
#     5) Data types of each column3

# 2. Write a program to:
#     1) Display total number of students in the dataset
#     2) Count how many students Passed (FinalResult = 1)
#     3) Count how many students Failed (FinalResult = 0)

# 3. Using pandas functions, calculate and display:
#     1) Average StudyHours
#     2) Average Attendance
#     3) Maximum PreviousScore
#     4) Maximum SleepHours

# 4. Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail Students.
# Is the dataset balanced? Justify your answer.

import pandas as  pd

Border = "-"*40

###########################################################################################
# Step 1 : Load the dataset
###########################################################################################

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

###########################################################################################
# Step 2 : Data Analysis
###########################################################################################

print(Border)
print("Step 2 : Data (Result) Analysis")
print(Border)

total_students = df.shape[0]
print("Total number of students :", total_students)

passed_students = df[df["FinalResult"] == 1].shape[0]
print("Number of students Passed :", passed_students)

failed_students = df[df["FinalResult"] == 0].shape[0]
print("Number of students Failed :", failed_students)

###########################################################################################
# Step 3 : Statistical Calculations (Define Independent and Dependent Variable)
###########################################################################################

print(Border)
print("Step 3 : Statistical Calculations")
print(Border)

avg_study_hours = df["StudyHours"].mean()
print("Average StudyHours :", avg_study_hours)

avg_attendance = df["Attendance"].mean()
print("Average Attendance :", avg_attendance)

max_previous_score = df["PreviousScore"].max()
print("Maximum PreviousScore :", max_previous_score)

max_sleep_hours = df["SleepHours"].max()
print("Maximum SleepHours :", max_sleep_hours)

###########################################################################################
# Step 4 : Distribution Analysis of FinalResult
###########################################################################################

print(Border)
print("Step 4 : Distribution Analysis")
print(Border)

result_counts = df["FinalResult"].value_counts()

print("FinalResult Distribution:")
print(result_counts)

# Calculate percentages
total_students = df.shape[0]

pass_percentage = (result_counts.get(1, 0) / total_students) * 100
fail_percentage = (result_counts.get(0, 0) / total_students) * 100

print("\nPass Percentage : {:.2f}%".format(pass_percentage))
print("Fail Percentage : {:.2f}%".format(fail_percentage))

###########################################################################################
# Check if dataset is balanced
###########################################################################################

if abs(pass_percentage - fail_percentage) <= 10:
    print("\nDataset is Balanced (Pass and Fail percentages are close).")
else:
    print("\nDataset is Imbalanced (Large difference between Pass and Fail percentages).")