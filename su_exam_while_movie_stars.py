total_budget = float(input())

while True:
    command = input()
    if command == 'ACTION':
        break
    if len(command) > 15:
        salary = total_budget * .2
        total_budget -= salary
        continue
    salary = float(input())
    total_budget -= salary
    if total_budget <= 0:
        break
if total_budget >= 0:
    print(f'We are left with {total_budget:.2f} leva. ')
else:
    print(f'We need {total_budget * -1 :.2f} leva for our actors.')

budget = float(input())
command = input()

# CHATGPT:
# budget = float(input())
# command = input()
#
# while command != "ACTION":
#     actor_name = command
#     payment = float(input())
#
#     if len(actor_name) <= 15:
#         budget -= payment
#     else:
#         budget -= payment + (0.2 * budget)
#
#     if budget < 0:
#         needed_budget = abs(budget)
#         print(f"We need {needed_budget:.2f} leva for our actors.")
#         break
#
#     command = input()
#
# if budget >= 0:
#     print(f"We are left with {budget:.2f} leva.")

