# def increment_version(version_str):
#     n1, n2, n3 = map(int, version_str.split('.'))
#     n3 += 1
#     if n3 > 9:
#         n3 = 0
#         n2 += 1
#     if n2 > 9:
#         n2 = 0
#         n1 += 1
#     next_version = f"{n1}.{n2}.{n3}"
#     return next_version
#
# current_version = input()
# next_version = increment_version(current_version)
# print(next_version)
#
#

# ANOTHER ONE:

# version = input()
# version_int = version.replace(".", "")
# next_version = int(version_int) + 1
# print(".".join(str(next_version)))
# ne e napylno pravilno, poneje ne dava 10.0.0, a 1.0.0.0


# ANOTHER ONE:

version = [int(digit) for digit in input().split('.')]
version[-1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print('.'.join(str(number) for number in version))
