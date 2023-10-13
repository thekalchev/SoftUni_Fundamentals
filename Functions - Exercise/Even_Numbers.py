sequence = input().split()
sequence_as_even_integers = []
for i in sequence:
    num = int(i)
    if num % 2 == 0:
        sequence_as_even_integers.append(num)
print(sequence_as_even_integers)

