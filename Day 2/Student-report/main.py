# program : A student report generator
# problem : Manual calculation takes time and creates room for mistakes
# solution : Fast, accurate and efficient generation of report. saves time and effort
# future improvements : make this program save the history of each report generation with their specific exam name and dates in a database.
#                       after recording the database, we can predict which student might top the next exam.

import students
import grades
import utils

student_name = students.get_student_name()
student_roll_no = students.get_student_roll_no()
student_marks = {}
student_marks = students.get_student_marks()

total_mark = grades.calculate_total(student_marks)
average_mark = grades.calculate_average(student_marks)
student_grade = grades.calculate_grade(student_marks)

utils.print_report(student_name, student_roll_no, student_marks, total_mark, average_mark, student_grade)