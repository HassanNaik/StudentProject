import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



# -----------------------------------------------------------------------------------
#                             Box Plots and Histogram Data
# -----------------------------------------------------------------------------------


# Read the CSV file
df = pd.read_csv('studentperformancefactors.csv')

# Extract 'Exam_Score' column
exam_scores = df['Exam_Score']

# Extract 'Attendance' column
attendance = df['Attendance']

# Extract 'Hours_Studied' column
study = df['Hours_Studied']

# Plot the box plot
# plt.figure(figsize=(10, 6))
# plt.boxplot(exam_scores, vert=False, patch_artist=True)
# plt.title('Box Plot of Exam Score')
# plt.xlabel('Exam Score')
# plt.savefig("Exam_Score_Boxplot.png")
# plt.show()

# # Plot the histogram
# plt.figure(figsize=(10, 6))
# plt.hist(exam_scores, bins=10, edgecolor='black')
# plt.title('Histogram of Exam Scores')
# plt.xlabel('Exam Score')
# plt.ylabel('Frequency')
# plt.savefig("Exam_Score_Histogram.png")
# plt.show()


# Plot the box plot for Attendance
# plt.figure(figsize=(10, 6))
# plt.boxplot(attendance, vert=False, patch_artist=True)
# plt.title('Box Plot of Attendance')
# plt.xlabel('Attendance')
# plt.savefig("Attendance_Boxplot.png")
# plt.show()

# Plot the histogram for Attendance
# plt.figure(figsize=(10, 6))
# plt.hist(attendance, bins=10, edgecolor='black')
# plt.title('Histogram of Attendance')
# plt.xlabel('Attendance')
# plt.ylabel('Frequency')
# plt.savefig("Attendance_Histogram.png")
# plt.show()


# Plot the box plot for Study Hours
# plt.figure(figsize=(10, 6))
# plt.boxplot(study, vert=False, patch_artist=True)
# plt.title('Box Plot of Study Hours')
# plt.xlabel('Study Hours')
# plt.savefig("Study_Hours_Boxplot.png")
# plt.show()

# Plot the histogram for Study Hours
# plt.figure(figsize=(10, 6))
# plt.hist(study, bins=10, edgecolor='black')
# plt.title('Histogram of Study Hours')
# plt.xlabel('Study Hours')
# plt.ylabel('Frequency')
# plt.savefig("Study_Hours_Histogram.png")
# plt.show()

# Plot a box plot using seaborn
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Attendance', y='Exam_Score', data=df)
# plt.title('Box Plot of Exam Score based on Attendance')
# plt.xlabel('Attendance')
# plt.ylabel('Exam Score')
# plt.savefig("Attendance_vs_Exam_Score_Boxplot.png")
# plt.show()

# Plot a box plot using seaborn for Study Hours vs Exam Score
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Hours_Studied', y='Exam_Score', data=df)
# plt.title('Box Plot of Exam Score based on Study Hours')
# plt.xlabel('Study Hours')
# plt.ylabel('Exam Score')
# plt.savefig("Study_Hours_vs_Exam_Score_Boxplot.png")
# plt.show()


# Plot a box plot using seaborn for Parental Involvement vs Exam Score
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Parental_Involvement', y='Exam_Score', data=df)
# plt.title('Box Plot of Exam Score based on Parental Involvement')
# plt.xlabel('Parental Involvement')
# plt.ylabel('Exam Score')
# plt.savefig("Parental_Involvement_vs_Exam_Score_Boxplot.png")
# plt.show()


# Plot a histogram for Exam Score based on Attendance
# plt.figure(figsize=(10, 6))
# attendance_groups = df.groupby('Attendance')['Exam_Score'].apply(list)
# for group in attendance_groups.index:
#     plt.hist(attendance_groups[group], bins=10, alpha=0.5, label=f'Attendance: {group}')
# plt.title('Histogram of Exam Score based on Attendance')
# plt.xlabel('Exam Score')
# plt.ylabel('Frequency')
# plt.legend()
# plt.savefig("Attendance_vs_Exam_Score_Histogram.png")
# plt.show()

# Plot a histogram for Exam Score based on Study Hours
# plt.figure(figsize=(10, 6))
# study_groups = df.groupby('Hours_Studied')['Exam_Score'].apply(list)
# for group in study_groups.index:
#     plt.hist(study_groups[group], bins=10, alpha=0.5, label=f'Study Hours: {group}')
# plt.title('Histogram of Exam Score based on Study Hours')
# plt.xlabel('Exam Score')
# plt.ylabel('Frequency')
# plt.legend()
# plt.savefig("Study_Hours_vs_Exam_Score_Histogram.png")
# plt.show()

# # Plot a histogram for Exam Score based on Parental Involvement
plt.figure(figsize=(10, 6))
parental_groups = df.groupby('Parental_Involvement')['Exam_Score'].apply(list)
for group in parental_groups.index:
    plt.hist(parental_groups[group], bins=10, alpha=0.5, label=f'Parental Involvement: {group}')
plt.title('Histogram of Exam Score based on Parental Involvement')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')
plt.legend()
plt.savefig("Parental_Involvement_vs_Exam_Score_Histogram.png")
plt.show()
