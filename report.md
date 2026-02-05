# Student Performance Analyzer – Project Report

## 1. Introduction
The Student Performance Analyzer project focuses on analyzing academic
performance using data-driven techniques. The objective is to understand
how factors such as study hours, attendance, part-time jobs, academic
major, and extracurricular activities influence student GPA.

The entire analysis is implemented using NumPy to strengthen foundational
data analysis skills.

---

## 2. Dataset Description
The dataset contains academic and demographic information of students.
The attributes include:
- Student ID
- Gender
- Age
- Study Hours
- Attendance Percentage
- GPA
- Academic Major
- Part-Time Job Status
- Extracurricular Activities Participation

---

## 3. Methodology
- The dataset was loaded using NumPy’s genfromtxt function.
- Numerical columns were extracted and converted for analysis.
- Boolean masking and indexing were used to filter data.
- Statistical analysis was performed to calculate mean, minimum, and
  maximum GPA.
- Correlation analysis was conducted using NumPy’s corrcoef function.
- Group-wise analysis was used for majors, part-time jobs, and
  extracurricular activities.

---

## 4. Results and Observations

### 4.1 Statistical Analysis
- Average GPA: 2.99
- Highest GPA: 3.99
- Lowest GPA: 2.00

### 4.2 Top and Weak Performing Students
- The top-performing student achieved a GPA of 3.99.
- The weak-performing student had a GPA of 2.00.

### 4.3 Correlation Analysis
- Study Hours vs GPA correlation: 0.09
- Attendance vs GPA correlation: 0.06

These results indicate weak but positive relationships, suggesting that
these factors influence GPA but are not the only contributors.

### 4.4 Part-Time Job Analysis
- Average GPA (With Job): 3.01
- Average GPA (Without Job): 2.96

Students with part-time jobs show slightly better performance, indicating
effective time management.

### 4.5 Major-Wise GPA Analysis
- Arts: 3.01
- Business: 3.04
- Education: 2.94
- Engineering: 2.97
- Science: 2.96

Academic performance varies across majors due to differing academic
demands and learning patterns.

### 4.6 Extracurricular Activities Analysis
- Participating students average GPA: 3.01
- Non-participating students average GPA: 2.96

Participation in extracurricular activities does not negatively affect
academic performance and may improve overall skills.

---

## 5. Conclusion
The analysis shows that student performance depends on a combination of
academic habits and lifestyle factors. Balanced study routines,
participation in activities, and time management play a key role in
overall academic success.

---

## 6. Future Scope
- Perform the same analysis using Pandas
- Add visualizations using Matplotlib
- Build an interactive dashboard using Streamlit
- Apply predictive models using machine learning techniques

---

## 7. Author
Shravya Hegade  
AI & Data Science Student
