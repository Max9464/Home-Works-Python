# from random import randint
# import random
#
# print('\n-----<<Hi this is candy game!>>-----' +
#       '\nTake you candy and Winn,' + '\nHo is take last candy'+'\n-----------<<CANDY KING!>>----------')
#
# print("\nHi, my name is CANDY KILLER ")
#
# name_player = input('\nWhat is you name? ')
# print("\n      let's figte " + name_player.upper()+'!')
# bot = 'CANDY KILLER'
#
# players_random = bot, name_player
# ho_is_first = random.choice(players_random)
# start_number = randint(100, 150)
#
#
# print('\n' + ho_is_first.upper() + ' is First!')
# print("This is a candy number's: " + str(start_number) + " candy's")
#
# # If bot going first
# if ho_is_first == bot:
#     bot_hod = randint(1, 28)
#     print('CANDY KILLER: -'+str(bot_hod))
#     count = start_number - bot_hod
#     start_number = count
#     print('\n----------------<< ' + str(count) + ' >>----------------')
#     print('\nNext Player: ' + name_player.upper())
#
#     while True:
# # Player_2 hod
#         player_2 = int(input(name_player.upper() + ' Take you candy from 1 to 28: '))
#         while player_2 > 28:
#             print('--------------- ERROR! ---------------- ')
#             player_2 = int(input('Take candy from 1 to 28: '))
#         count = start_number - player_2
#         start_number = count
# # Cheking Winner
#         if count <= 0:
#             print('')
#             ('               ' + str(name_player.upper()))
#             print('\n<<---------->> YOU WINNER! <<----------->> ')
#             break
#         print('\n----------------<< ' + str(count) + ' >>----------------')
#         print('\nNext Player: ' + bot)
# # Bot hod
#         if count == 56:
#             bot_hod = 27
#             count = start_number - bot_hod
#             start_number = count
#         elif count < 56:
#             bot_hod = randint(1, 5)
#             count = start_number - bot_hod
#             start_number = count
#             if count <= 28:
#                 bot_hod = start_number
#                 count = start_number - start_number
#                 start_number = count
#
#         else:
#             bot_hod = randint(9, 28)
#         print('CANDY KILLER: -' + str(bot_hod))
#         count = start_number - bot_hod
#         start_number = count
# # Cheking Winner
#         if count <= 0:
#             print('')
#             print('              ' + str(bot))
#             print('\n<<---------->> YOU WINNER! <<----------->> ')
#             break
#         print('\n----------------<< ' + str(count) + ' >>----------------')
#         print('\nNext Player: ' + name_player.upper())
#
# # If Second player "name_player" going first
# else:
#     player_2 = int(input(name_player.upper() + ' Take you candy from 1 to 28: '))
#     while player_2 > 28:
#         print('--------------- ERROR! ---------------- ')
#         player_2 = int(input('Take candy from 1 to 28: '))
#     count = int(start_number) - player_2
#     start_number = count
#     print('\n----------------<< ' + str(count) + ' >>----------------')
#     print('\nNext Player: ' + bot)
#
#     while True:
# # Bot hod
#         if count == 56:
#             bot_hod = 27
#             count = start_number - bot_hod
#             start_number = count
#         elif count < 56:
#             bot_hod = randint(1, 5)
#             count = start_number - bot_hod
#             start_number = count
#             if count <= 28:
#                 bot_hod = start_number
#                 count = start_number - start_number
#                 start_number = count
#
#         else:
#             bot_hod = randint(9, 28)
#         print('CANDY KILLER: -' + str(bot_hod))
#         count = start_number - bot_hod
#         start_number = count
# # Cheking Winner
#         if count <= 0:
#             print('')
#             print('              ' + str(bot))
#             print('\n<<---------->> YOU WINNER! <<----------->> ')
#             break
#         print('\n----------------<< ' + str(count) + ' >>----------------')
#         print('\nNext Player: ' + name_player.upper())
# # Player_2 hod
#         player_2 = int(input(name_player.upper() + ' Take you candy from 1 to 28: '))
#         while player_2 > 28:
#             print('--------------- ERROR! ---------------- ')
#             player_2 = int(input('Take candy from 1 to 28: '))
#         count = start_number - player_2
#         start_number = count
# # Cheking Winner
#         if count <= 0:
#             print('')
#             ('                 ' + str(name_player))
#             print('\n<<---------->> YOU WINNER! <<----------->> ')
#             break
#         print('\n----------------<< ' + str(count) + ' >>----------------')
#         print('\nNext Player: ' + bot)

#==================================== КРЕСТИКИ НОЛИКИ ==================================================

# maps = [0, 1, 2,
#         3, 4, 5,
#         6, 7, 8]
#
# victories = [[0, 1, 2,
#               3, 4, 5,
#               6, 7, 8,
#               0, 3, 6,
#               1, 4, 7,
#               2, 5, 8,
#               0, 4, 8,
#               2, 4, 6]]
#
# def print_maps():
#     print(maps[0], end=' ')
#     print(maps[1], end=' ')
#     print(maps[2])
#
#     print(maps[3], end=' ')
#     print(maps[4], end=' ')
#     print(maps[5])
#
#     print(maps[6], end=' ')
#     print(maps[7], end=' ')
#     print(maps[8])
# print(print_maps())
#
# def step_map(step, symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
#
# def get_result():
#     win = ''
#
#     for i in victories:
#         if maps[i[0]] == 'x' and maps[i[1]] == 'x' and maps[i[2]] == 'x':
#             win = 'x'
#         if maps[i[0]] == 'o' and maps[i[1]] == 'o' and maps[i[2]] == 'o':
#             win = 'o'
#         return win
#
# def check_line(sum_o, sum_x):
#
#     step = ''
#     for line in victories:
#         o = 0
#         x = 0
#
#         for j in range(0, 3):
#             if maps[line[j]] == 'o':
#                 o = 0 + 1
#             if o == sum_o and x == sum_x:
#                 for j in range(0, 3):
#                     if maps[line[j]] != 'o' and maps[line[j]] != 'x':
#                         step = maps[line[j]]
#     return step
#
# def AI():
#     step = ''
#
#     step = check_line(2, 0)
#     if step == '':
#         step = check_line(0, 2)
#     if step == '':
#         step = check_line(1, 0)
#     if step == '':
#        if maps[4] != 'x' and maps[4] != 'o':
#            step = 4
#     if step == '':
#        if maps[0] != 'x' and maps[0] != 'o':
#            step = 0
#
#     return step
# game_over = False
# human = True
# name = input(" Input you name: ")
# while game_over == False:
#     print_maps()
#     if human == True:
#         symbol = 'x'
#         step = int(input(name.title() + ":  "))
#     else:
#         print("Bot's tern: ")
#         symbol = 'o'
#         step = AI()
#     if step != '':
#         step_map(step, symbol)
#         win = get_result()
#         if win != '':
#             game_over = True
#         else:
#             game_over = False
#     else:
#         print("No body win")
#         game_over = True
#         win = "Frens"
#     human = not(human)
# print_maps()
# print("Win", win)

#================================== Реализуйте RLE алгоритм ==========================

def main():
    """Demo usage of functions."""
    rle = input("input: ")
    encoded = encode(rle)
    decoded = decode(encoded)

    print("Test Vector: " + rle)

    # Expected output: 12WB12W3B24WB14W
    print("Encoded Result: " + formatOutput(encoded))

    # Expected output = rel
    print("Decoded Result: " + decoded)


def encode(sequence):
    """Encode a sequence of characters and return the result as a list of tuples (data value and number of observed instances of value).
    Keyword arguments:
    sequence -- a sequence of characters to encode represented as a string.
    """
    count = 1
    result = []

    for x, item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1

    result.append((sequence[len(sequence) - 1], count))

    return result


def decode(sequence):
    """Decodes the sequence and returns the result as a string.
    Keyword arguments:
    sequence -- a list of tuples (data value and number of observed instances of value).
    """
    result = []

    for item in sequence:
        result.append(item[0] * item[1])

    return "".join(result)


def formatOutput(sequence):
    """Returns a print friendly version of the encoded data.
    Keyword arguments:
    sequence -- list of tuples (data value and number of observed instances of value).
    """
    result = []

    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])

    return "".join(result)


if __name__ == "__main__":
    main()
































