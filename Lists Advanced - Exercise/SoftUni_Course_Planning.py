def add_lesson(schedule, lesson):
    if lesson not in schedule:
        schedule.append(lesson)

def insert_lesson(schedule, lesson, index):
    if 0 <= index < len(schedule) and lesson not in schedule:
        schedule.insert(index, lesson)

def remove_lesson(schedule, lesson):
    if lesson in schedule:
        index = schedule.index(lesson)
        schedule.pop(index)
        if index < len(schedule) and schedule[index].endswith("-Exercise"):
            schedule.pop(index)

def swap_lessons(schedule, lesson1, lesson2):
    if lesson1 in schedule and lesson2 in schedule:
        index1 = schedule.index(lesson1)
        index2 = schedule.index(lesson2)
        schedule[index1], schedule[index2] = schedule[index2], schedule[index1]

def add_exercise(schedule, lesson):
    exercise = f"{lesson}-Exercise"
    if lesson in schedule:
        index = schedule.index(lesson)
        if index + 1 < len(schedule) and not schedule[index + 1].endswith("-Exercise"):
            schedule.insert(index + 1, exercise)
        else:
            schedule.insert(index + 1, exercise)
    else:
        schedule.append(lesson)
        schedule.append(exercise)

initial_schedule = input().split(', ')
commands = input()

while commands != "course start":
    command, *args = commands.split(":")
    if command == "Add":
        add_lesson(initial_schedule, args[0])
    elif command == "Insert":
        insert_lesson(initial_schedule, args[0], int(args[1]))
    elif command == "Remove":
        remove_lesson(initial_schedule, args[0])
    elif command == "Swap":
        swap_lessons(initial_schedule, args[0], args[1])
    elif command == "Exercise":
        add_exercise(initial_schedule, args[0])

    commands = input()

for i, lesson in enumerate(initial_schedule, start=1):
    print(f"{i}.{lesson}")
