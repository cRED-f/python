##list comprehension
# num_list=[1,2,3]
# new_num_list=[item+1  for item in num_list]
# print(new_num_list)
#
#
# names=["fahim","jahid","asif","mark","jhonny","naif","jihan"]
# short_names=[n for n in names if len(n)<5]
# print(short_names)
#
# long_name=[n.upper() for n in names if len(n)==5]
# print(long_name)


# dictionary comprehension
# new_dictionary={new_key:new_value for (key,value) in dictionary.item() if test}

import pandas
import random
# names = ["fahim", "Zahid", "asif", "mark", "johnny", "naif", "Cihan"]
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
#
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
