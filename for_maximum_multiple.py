divisor = int(input())
boundary = int(input())
# number = 0
# for num in range(boundary + 1):
#     if num > 0:
#         if num % divisor == 0:
#             number = num
# print(number)

#kato trygnem naobratno - pyrvoto sreshtnato chislo e otgovoryt, poneje
#tyrsim nai- golqmoto vyzmojno chislo, otgovarqshto na usloviqta
for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break
print(number)

