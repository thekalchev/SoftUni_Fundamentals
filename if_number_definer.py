number = float(input())
# if number == 0:
#     print('zero')
# elif 0 < number < 1:
#     print('small ', end='')
# elif -1 < number < 0:
#     print('small ', end='')
# elif abs(number) > 1000000:
#     print('large ', end='')
# if number > 0:
#     print('positive')
# if number < 0:
#     print('negative')

if number == 0:
    print('zero')
elif number > 0:
    if number < 1:
        print('small positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')