def perfect_number_checker(number: int):
    sum_of_divisors = 0
    for n in range(1, number):
        if number % n == 0:
            sum_of_divisors += n
    if sum_of_divisors == number:
        return 'We have a perfect number!'
    return "It's not so perfect."


num = int(input())
print(perfect_number_checker(num))