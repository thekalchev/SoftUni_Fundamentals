number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_student_attendances = 0

for student in range(number_of_students):
    attendances = int(input())
    total_bonus = attendances / number_of_lectures * (5 + additional_bonus)

    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        max_student_attendances = attendances

print(f'Max Bonus: {int(max_bonus)}.')
print(f'The student has attended {max_student_attendances} lectures.')
