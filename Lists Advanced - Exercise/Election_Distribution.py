# number_of_electrons = int(input())
# shell_number = 0
# list_of_shells = []
# while number_of_electrons > 0:
#     shell_number += 1
#     max_electrons = 2 * (shell_number ** 2)
#     if number_of_electrons < max_electrons:
#         if number_of_electrons > 0:
#             list_of_shells.append(number_of_electrons)
#             break
#         else:
#             break
#     else:
#         number_of_electrons -= max_electrons
#         list_of_shells.append(max_electrons)
# print(list_of_shells)
#
# # def distribute_electrons(number_of_electrons):
# #     shell_number = 1
# #     list_of_shells = []
# #
# #     while number_of_electrons > 0:
# #         max_electrons_in_shell = 2 * shell_number**2
# #         if number_of_electrons >= max_electrons_in_shell:
# #             list_of_shells.append(max_electrons_in_shell)
# #             number_of_electrons -= max_electrons_in_shell
# #         else:
# #             list_of_shells.append(number_of_electrons)
# #             break
# #         shell_number += 1
# #
# #     return list_of_shells
# #
# # number_of_electrons = int(input())
# # result = distribute_electrons(number_of_electrons)
# #
# # print(result)

number_of_electrons = int(input())
shells = []
for shell in range(1, number_of_electrons + 1):
    max_electrons_in_current_shell = 2 * shell ** 2
    if number_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        number_of_electrons -= max_electrons_in_current_shell
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)
