movie_count = 0
value = 0
best_value = 0
best_movie = ''
while True:
    movie_name = input()
    movie_count += 1
    if movie_name == 'STOP':
        break
    elif movie_count >= 7:
        print(f'The limit is reached.')
        break
    for i in movie_name:
        value += ord(i)
        if i.islower():
            value -= 2 * len(movie_name)
        elif i.isupper():
            value -= len(movie_name)
    if value > best_value:
        best_value = value
        best_movie = movie_name
    value = 0
print(f'The best movie for you is {best_movie} with {best_value} ASCII sum.')
