number_of_pieces = int(input())
info = {}
for current_piece in range(number_of_pieces):
    piece, composer, key = input().split('|')
    info[piece] = (composer, key)
while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece not in info:
            info[piece] = (composer, key)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f'{piece} is already in the collection!')
    elif command[0] == 'Remove':
        piece = command[1]
        if piece in info:
            del info[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif command[0] == 'ChangeKey':
        piece, new_key = command[1], command[2]
        if piece in info:
            info[piece] = (info[piece][0], new_key)
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
for pieces in (info):
    print(f'{pieces} -> Composer: {info[pieces][0]}, Key: {info[pieces][1]}')