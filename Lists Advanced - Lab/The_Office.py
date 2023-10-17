# employees_happiness = list(map(int, input().split()))
# happiness_factor = int(input())
# total_count = len(employees_happiness)
# multiplied_happiness = []
# for i in employees_happiness:
#     multiplied_happiness.append(happiness_factor * i)
# average_sum_of_happiness = sum(multiplied_happiness) / total_count
# happy_count = [happier for happier in multiplied_happiness if happier >= average_sum_of_happiness]
# if len(happy_count) >= total_count / 2:
#     print(f'Score: {len(happy_count)}/{total_count}. Employees are happy!')
# else:
#     print(f'Score: {len(happy_count)}/{total_count}. Employees are not happy!')
def check_employee_happiness():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())
    improved_happiness = [happiness * happiness_factor for happiness in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(happiness >= average_happiness for happiness in improved_happiness)
    total_count = len(improved_happiness)
    message = 'happy' if happy_count >= total_count / 2 else 'not happy'
    result = f'Score: {happy_count}/{total_count}. Employees are {message}!'
    return result


print(check_employee_happiness())
