# paranthesis should be (), nested aren't allowed
num_of_lines = int(input())
left_paranthesis = 0
right_paranthesis = 0
for i in range(num_of_lines):
    symbol = input()
    if symbol == '(':
        left_paranthesis += 1
    elif symbol == ')':
        right_paranthesis += 1
    if left_paranthesis - right_paranthesis >= 2:
        print('UNBALANCED')
        exit()
if left_paranthesis == right_paranthesis:
    print('BALANCED')
else:
    print('UNBALANCED')
