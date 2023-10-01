# two teams - A and B have 11 players each, numbered 1 to 11
# if one team has less than 7 players, the game stops, the team loses
# a card is a string with team's letter, followed by - and a player's #

team_a = ['A-' + str(s) for s in range(1, 12)]
team_b = ['B-' + str(s) for s in range(1, 12)]
players = input().split()
game_was_terminated = False
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if game_was_terminated:
    print('Game was terminated')


# A_players_count = 11
# B_players_count = 11
# string_of_cards = input()
# players = list(string_of_cards.split())
# for i in players:
#     if i[0] == 'A':  # if the element's name begins with A
#         A_players_count -= 1
#         if A_players_count < 7:
#             break
#     elif i[0] == 'B':
#         B_players_count -= 1
#         if B_players_count < 7:
#             break
# print(f'Team A - {A_players_count}; Team B - {B_players_count}')
# if A_players_count < 7 or B_players_count < 7:
#     print('Game was terminated')
