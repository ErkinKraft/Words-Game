import random
from art import tprint
import time
tprint('Words game V1.0')
print('GitHub > https://github.com/ErkinKraft')

print('More bugs')

time.sleep(3)
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')

# Создаем список слов для угадывания
words = ['яблоко', 'апельсин', 'банан', 'груша', 'киви', 'ананас', 'хуй', 'очко', 'вова', 'игра', 'пубг', 'елисей', 'питон', 'бобёр', 'кавасаки', 'крико', ' каго', 'стрипер', 'негр', 'суслик', 'майнкрафт', 'едит', '4090', 'ай5']

def play_game():
    # Выбираем случайное слово из списка
    word = random.choice(words)
    # Создаем пустую строку для отображения угадываемого слова
    guessed_word = '_' * len(word)
    # Конвертируем строку в список символов, чтобы было удобнее менять значения
    guessed_word_list = list(guessed_word)
    # Создаем список для хранения уже угаданных букв
    guessed_letters = []

    # Счетчик для подсчета количества оставшихся попыток
    attempts = 7

    print(f'Угадайте слово: {guessed_word}')

    while attempts > 0:
        # Запрос от пользователя для ввода буквы
        letter = input('Введите букву: ').lower()
        if letter == 'adminmodeon':
            passin = input('Password> ')
            if passin == 'es':

                while True:
                    print('Admin mode on')
                    print('')
                    print('1. edit attempt')
                    print('')
                    print('2. ? dot')
                    print('')
                    print('3. play')
                    print('')
                    print('4. custom word')
                    com1 = input('> ')
                    if com1 == '1':
                        attempts = int(input('attempts> '))
                    else:
                        print(' ')

                    if com1 == '2':
                        guessed_word = input('? dot>')
                    else:
                        print('')

                    if com1 == '3':
                        break
                    else:
                        print('')
                    if com1 == '4':
                        guessed_word_list = input('custom word> ')
                    else:
                        print("")
            else:
                print('')



        else:  print('')

        if len(letter) > 1:
            print('Пожалуйста, введите только одну букву!')
            continue

        if letter in guessed_letters:
            print('Вы уже угадали эту букву!')
            continue

        guessed_letters.append(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word_list[i] = letter

            guessed_word = ''.join(guessed_word_list)

            print(f'Угадано! {guessed_word}')
        else:
            attempts -= 1
            print(f'Неугадано... У вас осталось {attempts} попыток.')

        if '_' not in guessed_word:
            print('Поздравляю, вы угадали слово!')
            if word == 'хуй':
                print('Сорян ну не мог без этого')
            break

    if attempts == 0:
        print(f'К сожалению, вы проиграли! Загаданное слово было: {word}.')


play_game()
