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

# 5. Based on the dataset values, analyze whether:
#     1) Higher StudyHours increase the change of passing.
#     2) Higher Attendance improve FinalResult.
#         Write your observations in 4-5 lines.

# 6. Plot a histogram of StudyHours.
#     Explain what the distribution tells you.

# 7. Create a scatter plot of:
#     StudyHours vs PreviousScore
#     Use different colors for Pass and Fail students.

import pandas as  pd
import matplotlib.pyplot as plt

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

###########################################################################################
# Step 5 : Analysis of StudyHours & Attendance vs FinalResult
###########################################################################################

print(Border)
print("Step 5 : Relationship Analysis")
print(Border)

study_analysis = df.groupby("FinalResult")["StudyHours"].mean()
print("Average StudyHours (0=Fail, 1=Pass):")
print(study_analysis)

print()

attendance_analysis = df.groupby("FinalResult")["Attendance"].mean()
print("Average Attendance (0=Fail, 1=Pass):")
print(attendance_analysis)

# Observation:
# The average StudyHours of failed students is 2.55 hours, while passed students studied significantly more, with an average of 6.37 hours.
# This shows that students who studied more hours had a much higher chance of passing.
# The average Attendance of failed students is 67.75%, whereas passed students had a higher attendance of 86.61%.
# This indicates that better attendance is strongly associated with improved academic performance.
# Therefore, both higher StudyHours and higher Attendance positively influence the FinalResult, increasing the chance of passing.

###########################################################################################
# Step 6 : Histogram of StudyHours
###########################################################################################

print(Border)
print("Step 6 : Histogram of StudyHours")
print(Border)

plt.figure(figsize=(8,5))
plt.hist(df["StudyHours"], bins=10, color="skyblue", edgecolor="black")

plt.title("Histogram of StudyHours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Observation
# The StudyHours are distributed roughly between 1 and 8 hours.
# Most students appear to study between 4 to 7 hours, as the middle bars are relatively higher.
# There are fewer students studying very low hours (1–2 hours), indicating that extremely low study time is less common.
# The distribution looks fairly spread out and slightly concentrated in the mid-to-higher range.
# This suggests that a majority of students spend a moderate to high number of hours studying, which may positively influence overall performance.

###########################################################################################
# Step 7 : Scatter Plot (StudyHours vs PreviousScore)
###########################################################################################

print(Border)
print("Step 7 : Scatter Plot")
print(Border)

# Separate Pass and Fail students
pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

plt.figure(figsize=(8,5))

# Fail students
plt.scatter(fail_students["StudyHours"], fail_students["PreviousScore"], color="red", label="Fail")

# Pass students
plt.scatter(pass_students["StudyHours"], pass_students["PreviousScore"], color="green", label="Pass")

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend()
plt.grid(True)

plt.show()