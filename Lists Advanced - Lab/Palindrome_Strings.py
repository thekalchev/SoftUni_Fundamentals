words = input().split()
palindrome = input()
palindromes_in_list = [word for word in words if word == ''.join(reversed(word))]
occurance_counter = palindromes_in_list.count(palindrome)
print(palindromes_in_list)
print(f'Found palindrome {occurance_counter} times')