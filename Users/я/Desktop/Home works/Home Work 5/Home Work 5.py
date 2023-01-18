from random import randint
import random

print('\n-----<<Hi this is candy game!>>-----' +
      '\nTake you candy and Winn,' + '\nHo is take last candy'+'\n-----------<<CANDY KING!>>----------')

print("\nHi, my name is CANDY KILLER ")

name_player = input('\nWhat is you name? ')
print("\n      let's figte " + name_player.upper()+'!')
bot = 'CANDY KILLER'

players_random = bot, name_player
ho_is_first = random.choice(players_random)
start_number = randint(100, 300)


print('\n' + ho_is_first.upper() + ' is First!')
print("This is a candy number's: " + str(start_number) + " candy's")

# Cod if bot going first
if ho_is_first == bot:
    bot_hod = randint(1, 28)
    print('CANDY KILLER: -'+str(bot_hod))
    count = start_number - bot_hod
    start_number = count
    print('\n----------------<< ' + str(count) + ' >>----------------')
    print('\nNext Player: ' + name_player.upper())

    while True:
# Player_2 hod
        player_2 = int(input(name_player.upper() + ' Take you candy from 1 to 28: '))
        while player_2 > 28:
            print('--------------- ERROR! ---------------- ')
            player_2 = int(input('Take candy from 1 to 28: '))
        count = start_number - player_2
        start_number = count
        if count <= 0:
            print('')
            ('               ' + str(name_player.upper()))
            print('\n<<---------->> YOU WINNER! <<----------->> ')
            break
        print('\n----------------<< ' + str(count) + ' >>----------------')
        print('\nNext Player: ' + bot)
# Bot hod
        if count == 56:
            bot_hod = 27
            count = start_number - bot_hod
        elif count <= 28:
            bot_hod = 0
            count = start_number * bot_hod
            start_number = count
        else:
            bot_hod = randint(1, 28)
        print('CANDY KILLER: -' + str(bot_hod))
        count = start_number - bot_hod
        start_number = count
# Cheking Winner
        if count <= 0:
            print('')
            print('              ' + str(bot))
            print('\n<<---------->> YOU WINNER! <<----------->> ')
            break
        print('\n----------------<< ' + str(count) + ' >>----------------')
        print('\nNext Player: ' + name_player.upper())

# Cod if Second player "name_player" going first
else:
    player_2 = int(input(name_player.upper() + ' Take you candy from 1 to 28: '))
    while player_2 > 28:
        print('--------------- ERROR! ---------------- ')
        player_2 = int(input('Take candy from 1 to 28: '))
    count = int(start_number) - player_2
    start_number = count
    print('\n----------------<< ' + str(count) + ' >>----------------')
    print('\nNext Player: ' + bot)

    while True:
# Bot hod
        if count == 56:
            bot_hod = 27
            count = start_number - bot_hod
        elif count <= 28:
            bot_hod = 0
            count = start_number * bot_hod
            start_number = count
        else:
            bot_hod = randint(1, 28)
        print('CANDY KILLER: -' + str(bot_hod))
        count = start_number - bot_hod
        start_number = count
# Cheking Winner
        if count <= 0:
            print('')
            print('              ' + str(bot))
            print('\n<<---------->> YOU WINNER! <<----------->> ')
            break
        print('\n----------------<< ' + str(count) + ' >>----------------')
        print('\nNext Player: ' + name_player.upper())
# Player_2 hod
        player_2 = int(input(name_player.upper() + ' Take you candy from 1 to 28: '))
        while player_2 > 28:
            print('--------------- ERROR! ---------------- ')
            player_2 = int(input('Take candy from 1 to 28: '))
        count = start_number - player_2
        start_number = count
        if count <= 0:
            print('')
            ('                 ' + str(name_player))
            print('\n<<---------->> YOU WINNER! <<----------->> ')
            break
        print('\n----------------<< ' + str(count) + ' >>----------------')
        print('\nNext Player: ' + bot)




