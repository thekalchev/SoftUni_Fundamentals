course_info = {}

while True:
    command = input()
    if command == 'end':
        break
    course, student = command.split(' : ')

    if course not in course_info:
        course_info[course] = []
    course_info[course].append(student)

for course, student in course_info.items():
    print(f'{course}: {len(student)}')
    for student in student:
        print(f'-- {student}')


