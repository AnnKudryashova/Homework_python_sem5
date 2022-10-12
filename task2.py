#Создайте программу для игры с конфетами человек против человека.
#Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота 'интеллектом'

import random

welcome_text = ('Приветствую всех на игре "Хватай конфеты!"\n'
                'Для начала я расскажу правила:\n'
                'Я даю Вам 150 конфет, вы берете их по очереди,\n'
                'за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет конфеты.\n')

print(welcome_text)

message = 'твоя очередь'

def player_vs_player():
    candies = 150
    max_take = 28
    count = 0
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = input('\nА твоего соперника?: ')

    print(f'\nНу что ж, {player_1} и  {player_2}, начнем игру !\n')
    print('\nДля начала опеределим, кто первый начнет игру.\n')

    x = random.randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю, {lucky}, ты ходишь первым !')

    while candies > 0:
        if count == 0:
            step = int(input(f'\n{message}, {lucky}:  '))
            if step > candies or step > max_take:
                step = int(input(
                    f'\nНе жадничай, можно взять только {max_take} конфет, {lucky}, попробуй еще раз: '))
            candies = candies - step
        if candies > 0:
            print(f'\nосталось еще {candies} конфет')
            count = 1
        else:
            print('Ура, кончились конфетки!')

        if count == 1:
            step = int(input(f'\n{message}, {loser}: '))
            if step > candies or step > max_take:
                step = int(input(
                    f'\nНе жадничай, можно взять только {max_take} конфет, {loser}, попробуй еще раз: '))
            candies = candies - step
        if candies > 0:
            print(f'\n Осталось еще {candies} конфет')
            count = 0
        else:
            print('Ура, конфетки кончились!')

    if count == 1:
        print(f'{loser} - победитель!')
    if count == 0:
        print(f'{lucky} - победитель!')

player_vs_player()

def player_vs_bot():
    candies = 150
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\nНу что ж, {player_1} и  {player_2}, начнем игру!\n')
    print('\nДля начала опеределим, кто первый начнет игру.\n')

    lucky = random.randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]}, ты ходишь первым !')

    while candies > 0:
        lucky += 1
        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {candies} конфет. \n{message}: ')

            if candies < 29:
                step = candies
            else:
                z = candies // 28
                step = candies - ((z*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = random.randint(1,28)
            print(step)
        else:
            step = int(input(f'\nХоди,  {players[lucky%2]} \n Осталось {candies} конфет, {message}:  '))
            while step > max_take or step > candies:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies = candies - step

    print(f'Осталось {candies} конфет \nПобедитель - {players[lucky%2]}')

player_vs_bot()
