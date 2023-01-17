from random import randint
import random

first_player = input('1st player' + '\nHi, enter you name: ')
second_player = input('2st player' + '\nHi, enter you name: ')

players_random = first_player.title(), second_player.title()
ho_is_first = random.choice(players_random)
start_number = randint(87, 1000)


print(ho_is_first + ' is First!')
print('This is start Number: ' + str(start_number))


while True:
    player_1 = int(input('Enter the number of candy from 1 to 28: '))
    while player_1 > 28:
        print('Error!')
        player_1 = int(input('Enter the number of candy from 1 to 28: '))
    count = start_number - player_1
    if count == 0:
        print('------------ YOU WINNER! ------------- ')
        break
    print('----------------- ' + str(count) + ' -----------------')
    print('<<Next Player>>')
    player_2 = int(input('Enter the number of candy from 1 to 28: '))
    while player_2 > 28:
        print('Error!')
        player_2 = int(input('Enter the number of candy from 1 to 28: '))
    count = count - player_2
    start_number = count
    if count == 0:
        print('------------ YOU WINNER! ------------- ')
        break
    print('----------------- ' + str(count) + ' -----------------')
    print('<<Next Player>>')
