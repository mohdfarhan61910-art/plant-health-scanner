import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(
    "student_dataset.csv",
    sep="\t",
    header=None,
    names=["Student", "Study_Hours", "Attendance", "Marks"]
)

print("========================================")
print(" STUDENT PERFORMANCE ANALYSIS SYSTEM ")
print("========================================")

# First 10 Rows
print("\nFirst 10 Rows")
print(df.head(10))

# Last 5 Rows
print("\nLast 5 Rows")
print(df.tail())

# Shape
print("\nShape of Dataset")
print(df.shape)

# Columns
print("\nColumn Names")
print(df.columns)

# Data Types
print("\nData Types")
print(df.dtypes)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Fill Missing Marks
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

print("\nMissing Values After Filling")
print(df.isnull().sum())

# Total Students
print("\nTotal Students")
print(len(df))

# Average Study Hours
avg_hours = df["Study_Hours"].mean()
print("\nAverage Study Hours")
print(avg_hours)

# Average Attendance
avg_attendance = df["Attendance"].mean()
print("\nAverage Attendance")
print(avg_attendance)

# Average Marks
avg_marks = df["Marks"].mean()
print("\nAverage Marks")
print(avg_marks)

# Highest Attendance
print("\nHighest Attendance")
print(df["Attendance"].max())

# Lowest Attendance
print("\nLowest Attendance")
print(df["Attendance"].min())

# Highest Marks
print("\nHighest Marks")
print(df["Marks"].max())

# Lowest Marks
print("\nLowest Marks")
print(df["Marks"].min())

# Student with Highest Marks
top_student = df[df["Marks"] == df["Marks"].max()]
print("\nStudent with Highest Marks")
print(top_student)

# Student with Lowest Marks
low_student = df[df["Marks"] == df["Marks"].min()]
print("\nStudent with Lowest Marks")
print(low_student)

# Students Above Average Marks
print("\nStudents Above Average Marks")
above_avg = df[df["Marks"] > avg_marks]
print(above_avg)

print("\nNumber of Students Above Average")
print(len(above_avg))

# Attendance Greater Than 90
print("\nStudents Having Attendance Greater Than 90")
high_attendance = df[df["Attendance"] > 90]
print(high_attendance)

# Number of Students with Attendance >90
print("\nTotal Students Having Attendance >90")
print(len(high_attendance))

# Top 10 Students
print("\nTop 10 Students According to Marks")
top10 = df.sort_values(by="Marks", ascending=False)
print(top10.head(10))

# Bottom 10 Students
print("\nBottom 10 Students According to Marks")
bottom10 = df.sort_values(by="Marks")
print(bottom10.head(10))

# Correlation
print("\nCorrelation Matrix")
print(df[["Study_Hours", "Attendance", "Marks"]].corr())

# Describe Dataset
print("\nStatistical Summary")
print(df.describe())

# Save Clean Dataset
df.to_csv("clean_student_dataset.csv", index=False)

print("\nClean Dataset Saved Successfully")

# -------------------------
# Graph 1
# -------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Student"].head(10), df["Marks"].head(10))
plt.title("Marks of First 10 Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()

# -------------------------
# Graph 2
# -------------------------
plt.figure(figsize=(6,5))
plt.hist(df["Marks"], bins=10)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# Graph 3
# -------------------------
plt.figure(figsize=(6,5))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# -------------------------
# Graph 4
# -------------------------
plt.figure(figsize=(6,5))
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

print("\n========================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("========================================")