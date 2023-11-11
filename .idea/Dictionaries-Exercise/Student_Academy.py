number_of_pairs_of_rows = int(input())
gradebook = {}
for _ in range(number_of_pairs_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in gradebook:
        gradebook[student_name] = []
    gradebook[student_name].append(student_grade)

for student, grade in gradebook.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        print(f'{student} -> {average_grade:.2f}')
