import re

number_of_attempts = int(input())

for password in range(number_of_attempts):
    check_password = input()
    pattern = r"^([\S]+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]+)<\1$"

    match = re.fullmatch(pattern, check_password)
    if match:
        encrypted_password = f"{match.group(2)}{match.group(3)}{match.group(4)}{match.group(5)}"
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")