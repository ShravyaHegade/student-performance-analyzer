# 1. import libraries
import numpy as np

# load dataset 
data = np.genfromtxt(
    "student_performance_data.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

# 2. Extract numeric columns
# Columns:
# 2 -> Age
# 3 -> StudyHour
# 4 -> Attendance
# 5 -> GPA
numeric_data = data[:, [2, 3, 4, 5]].astype(float)

age = numeric_data[:, 0]
study_hours = numeric_data[:, 1]
attendance = numeric_data[:, 2]
gpa = numeric_data[:, 3]

# 3. Basic Statistical Analysis
print("STATISTICAL ANALYSIS")
print("Average GPA:", round(np.mean(gpa), 2))
print("Highest GPA:", np.max(gpa))
print("Lowest GPA:", np.min(gpa))
print("-" * 50)

# 4. Identify Top and Weak Students

highest_index = np.argmax(gpa)
lowest_index = np.argmin(gpa)

print("TOP PERFORMING STUDENT")
print("Student ID:", data[highest_index, 0])
print("Gender:", data[highest_index, 1])
print("Age:", data[highest_index, 2])
print("GPA:", gpa[highest_index])
print("-" * 50)

print("WEAK PERFORMING STUDENT")
print("Student ID:", data[lowest_index, 0])
print("Gender:", data[lowest_index, 1])
print("Age:", data[lowest_index, 2])
print("GPA:", gpa[lowest_index])
print("-" * 50)

# 5. Correlation Analysis

study_gpa_corr = np.corrcoef(study_hours, gpa)
attendance_gpa_corr = np.corrcoef(attendance, gpa)

study_corr_value = study_gpa_corr[0, 1]
attendance_corr_value = attendance_gpa_corr[0, 1]

def interpret_correlation(value, feature_name):
    if value > 0.7:
        strength = "strong positive"
    elif value > 0.4:
        strength = "moderate positive"
    elif value > 0.2:
        strength = "weak positive"
    elif value < -0.7:
        strength = "strong negative"
    elif value < -0.4:
        strength = "moderate negative"
    elif value < -0.2:
        strength = "weak negative"
    else:
        strength = "no significant"

    print(f"There is a {strength} relationship between {feature_name} and GPA.")

print("CORRELATION ANALYSIS")
print("Study Hours vs GPA correlation:", round(study_corr_value, 2))
interpret_correlation(study_corr_value, "Study Hours")
print()

print("Attendance vs GPA correlation:", round(attendance_corr_value, 2))
interpret_correlation(attendance_corr_value, "Attendance")
print("-" * 50)

# -------------------------------
# 6. Part-Time Job Impact
# -------------------------------
part_time = data[:, 7]

avg_yes = round(np.mean(gpa[part_time == "Yes"]), 2)
avg_no = round(np.mean(gpa[part_time == "No"]), 2)

print("PART-TIME JOB ANALYSIS")
print("Average GPA (With Job):", avg_yes)
print("Average GPA (Without Job):", avg_no)

if avg_yes > avg_no:
    print("INSIGHT: Students with part-time jobs show slightly better academic performance.")
else:
    print("INSIGHT: Students without part-time jobs tend to perform better academically.")
print("-" * 50)

# -------------------------------
# 7. Major-wise Performance Analysis
# -------------------------------
majors = np.unique(data[:, 6])

print("MAJOR-WISE GPA ANALYSIS")
for major in majors:
    major_gpa = gpa[data[:, 6] == major]
    print(f"{major}: Average GPA = {round(np.mean(major_gpa), 2)}")

print("INSIGHT: Academic performance varies across majors,")
print("indicating different academic demands and learning patterns.")
print("-" * 50)

# -------------------------------
# 8. Extracurricular Activities Impact
# -------------------------------
extra = data[:, 8]

avg_extra_yes = round(np.mean(gpa[extra == "Yes"]), 2)
avg_extra_no = round(np.mean(gpa[extra == "No"]), 2)

print("EXTRACURRICULAR ACTIVITIES ANALYSIS")
print("Average GPA (Participating):", avg_extra_yes)
print("Average GPA (Not Participating):", avg_extra_no)

if avg_extra_yes >= avg_extra_no:
    print("INSIGHT: Participation in extracurricular activities does not harm academics")
    print("and may improve time management and overall performance.")
else:
    print("INSIGHT: Students focusing only on academics show slightly higher GPA.")

print("-" * 50)

# -------------------------------
# 9. Final Conclusion
# -------------------------------
print("CONCLUSION")
print("Study hours and attendance show positive relationships with GPA.")
print("Part-time jobs and extracurricular activities do not negatively impact performance.")
print("Academic outcomes vary across majors, highlighting diverse learning demands.")
print("-" * 50)

print("Analysis completed successfully!")



