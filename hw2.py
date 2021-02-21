import random as rnd

limit_grade = 100

student_1 = ["Behzat","Ç."]
student_2 = ["Tahsin","Yılmaz"]
student_3 = ["Harun","Sinanoğlu"]
student_4= ["Sabri","Özay"]
student_5 = ["İsmet Arif","Karasu"]

all_students = [student_1,student_2,student_3,student_4,student_5]

grades_1 = []
grades_2 = []
grades_3 = []
grades_4 = []
grades_5 = []

all_grades = [grades_1,grades_2,grades_3,grades_4,grades_5]

info = {}

for i in range(0,5,1):
    midterm = rnd.randrange(0,limit_grade,1)
    final = rnd.randrange(0, limit_grade, 1)
    homework = rnd.randrange(0, limit_grade, 1)
    all_grades[i].append(midterm)
    all_grades[i].append(final)
    all_grades[i].append(homework)


for i in range(0,5,1):
    current_student = all_students[i]
    student_1_name = current_student[0] + " " + current_student[1]

    current_grade = all_grades[i]
    info[student_1_name] = current_grade


names_averages = []
for i in range(0,5,1):
    current_key_list = list(info.keys())
    current_key = current_key_list[i]
    current_values = info[current_key]
    current_average = sum(current_values)/len(current_values)
    names_averages.append([current_key,current_average])

sorted_names_averages = sorted(names_averages,key = lambda x:x[1], reverse=True)
print(sorted_names_averages)

print("Congrats",sorted_names_averages[0][0],"!","You are the most succesful student.")

