num1 = int(input())
num2 = int(input())
counter = 0
for i in range(1):
    print(f'Before:')
    print(f'a = {num1}')
    print(f'b = {num2}')
    counter += 1
    if counter > 0:
        print(f'After:')
        print(f'a = {num2}')
        print(f'b = {num1}')

# Read two integer numbers
# a = int(input())
# b = int(input())
#
# # Print the values before the exchange
# print("Before:")
# print(f'a = {a}')
# print(f'b = {b}')
#
# # Exchange the values using a temporary variable
# temp = a
# a = b
# b = temp
#
# # Print the values after the exchange
# print("After:")
# print(f'a = {a}')
# print(f'b = {b}')