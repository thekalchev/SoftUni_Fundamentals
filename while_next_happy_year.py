# year = int(input())
# year_is_special = False
# while not year_is_special:
#     year += 1
#     year_as_string = str(year)
#     year_is_special = True
#     for digit in year_as_string:
#         if year_as_string.count(digit) != 1:
#             year_is_special = False
#             break
# print(year)

# vtori nachin: slojen i gaden
# year = int(input())
# while True:
#     year += 1
#     year_as_string = str(year)
#     repetition_counter = 0
#     for index, digit in enumerate(year_as_string):
#         for control_index in range(index + 1, len(year_as_string)):
#             if year_as_string[control_index] == digit:
#                 repetition_counter += 1
#                 break
#         if repetition_counter > 1:
#             break
#     if repetition_counter == 1:
#         break
# print(year)

# treti nachin:
year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        print(year)
        break
# proverqvame dali ima elementi v seta koito se povtarqt
# ako ima- dyljinata na seta shte e razlichna ot broq na cifrite v godinata
# poneje seta propuska ednakvite elementi i printira samo ediniq

