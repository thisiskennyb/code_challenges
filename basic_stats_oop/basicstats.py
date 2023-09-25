import statistics 

class Student:

    def __init__ (self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade


student_1 = Student('jim', 72)
student_2 = Student('rick', 88)
student_3 = Student('betty', 67)

std_obj_lst = [student_1, student_2, student_3]

def basic_stats(student_obj_list):
    grade_list = []
    for i in std_obj_lst:
        grade_list.append(i.get_grade())
    return (statistics.mean(grade_list), statistics.median(grade_list), statistics.mode(grade_list))

print(basic_stats(std_obj_lst))