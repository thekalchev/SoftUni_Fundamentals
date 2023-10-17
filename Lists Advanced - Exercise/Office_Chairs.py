# number_of_rooms = int(input())
# total_chairs = 0
# total_visitors = 0
# room = 0
# for room in range(number_of_rooms):
#     visitors_chairs = input().split()
#     visitors = int(visitors_chairs[1])
#     chairs = visitors_chairs[0]
#     room += 1
#     total_chairs += len(chairs)
#     total_visitors += visitors
#     if visitors > len(chairs):
#         print(f'{visitors-len(chairs)} more chairs needed in room {room}')
# if total_chairs >= total_visitors:
#     print(f'Game On, {total_chairs-total_visitors} free chairs left')
#

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f'{abs(difference)} more chairs needed in room {number_of_room}')
        free_chairs += difference
    return free_chairs


count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
