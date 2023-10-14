def perfect_number_checker(number: int):
    sum_of_divisors = 0
    for n in range(1, number + 1):
        if number % n == 0:
            if number != n:
                sum_of_divisors += n
    if sum_of_divisors == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


num = int(input())
perfect_number_checker(num)