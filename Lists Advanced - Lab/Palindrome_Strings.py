# words = input().split()
# palindrome = input()
# palindromes_in_list = [word for word in words if word == ''.join(reversed(word))]
# occurance_counter = palindromes_in_list.count(palindrome)
# print(palindromes_in_list)
# print(f'Found palindrome {occurance_counter} times')

def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome_word = input()
palindrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = palindrome_list.count(palindrome_word)
print(palindrome_list)
print(f'Found palindrome {palindrome_counter} times')
