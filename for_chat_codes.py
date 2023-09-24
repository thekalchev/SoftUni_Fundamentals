number_of_messages = int(input())
for current_message in range(number_of_messages):
    integer = int(input())
    if integer == 88:
        print('Hello')
    elif integer == 86:
        print('How are you?')
    elif integer < 88:
        print('GREAT!')
    else:
        print('Bye.')
