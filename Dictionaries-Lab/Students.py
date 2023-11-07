# table = {}
# while True:
#     info = input()
#     if ':' not in info:
#         if '_' not in info:
#             for key, value in table.items():
#                 for current_id, current_course in value.items():
#                     if current_course == info:
#                         print(f'{key} - {current_id}')
#             break
#
#         else:
#             first_word, second_word = info.split('_')
#             for key, value in table.items():
#                 for current_id, current_course in value.items():
#                     if first_word in current_course:
#                         print(f'{key} - {current_id}')
#             break
#
#     else:
#         student_name, student_ID, course = info.split(':')
#     table[student_name] = {student_ID: course}


students = []
course_to_search = None
while True:
    student_info = input()
    if ':' not in student_info:
        course_to_search = student_info
        break
    name, ID, course = student_info.split(':')
    students.append({'name': name, "ID": ID, 'course': course})
for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")
