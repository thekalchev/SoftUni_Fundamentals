# from sympy import isprime
# num1 = int(input())
# if isprime(num1):
#     print('True')
# else:
#     print('False')
isprime = False
num1 = int(input())
if num1 == 2:
    print(f'True')
    exit()
for num in range(2, num1):
    if num1 % num == 0:
        isprime = False
        break
    else:
        isprime = True
if isprime:
    print(f'True')
else:
    print(f'False')
