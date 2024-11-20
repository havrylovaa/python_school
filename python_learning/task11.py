# Даны два множества, представляющие наборы студентов, посещающих разные курсы.
#
# course1_students = {"Alice", "Bob", "Charlie", "David"}
# course2_students = {"Charlie", "David", "Edward", "Fiona"}
#
# Необходимо:
# Найти студентов, которые посещают оба курса.
# Найти студентов, которые посещают только один из двух курсов (т.е. разность множеств).

def task11():
    course1_students = {"Alice", "Bob", "Charlie", "David"}
    course2_students = {"Charlie", "David", "Edward", "Fiona"}
    students_both_courses = course1_students.intersection(course2_students)
    students_single_course = course1_students.symmetric_difference(course2_students)
    just_single_course= course1_students - course2_students
    print("Студенты, посещающие оба курса:", students_both_courses)
    print("Студенты, посещающие только один из курсов:", just_single_course)

if __name__ == '__main__':
    task11()
