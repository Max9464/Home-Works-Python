from random import randint
import random

print('\n-----<<Hi this is candy game!>>-----' +
      '\nTake you candy and Winn,' + '\nHo is take last candy'+'\n-----------<<CANDY KING!>>----------')

first_player = input('1st player' + '\nHi, enter you name: ')
second_player = input('\n2st player' + '\nHi, enter you name: ')

players_random = first_player.title(), second_player.title()
ho_is_first = random.choice(players_random)
start_number = randint(87, 1000)


print('\n' + ho_is_first.upper() + ' is First!')
print('This is start Number: ' + str(start_number))


while True:
    player_1 = int(input('Take you candy from 1 to 28: '))
    while player_1 > 28:
        print('--------------- ERROR! ---------------- ')
        player_1 = int(input('Take candy from 1 to 28: '))
    count = start_number - player_1
    if count <= 0:
        print('\n<<---------->> YOU WINNER! <<----------->> ')
        break
    print('----------------<< ' + str(count) + ' >>----------------')
    print('\n------------<< Next Player >>------------')
    player_2 = int(input('Take you candy from 1 to 28: '))
    while player_2 > 28:
        print('--------------- ERROR! ---------------- ')
        player_2 = int(input('Take candy from 1 to 28: '))
    count = count - player_2
    start_number = count
    if count <= 0:
        print('\n<<---------->> YOU WINNER! <<----------->> ')
        break
    print('----------------<< ' + str(count) + ' >>----------------')
    print('\n------------<< Next Player >>------------')
