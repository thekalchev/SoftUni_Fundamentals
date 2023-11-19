# import re
#
# pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
# dates = input()
# result = re.findall(pattern, dates)
# for match in result:
#     print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')
#

import re

pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
dates = input()
result = re.finditer(pattern, dates)
for match in result:
    print(f'Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}')



