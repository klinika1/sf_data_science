"""Игра угадай число.
Компьютер сам загадывает и угадывает число.
Ведется подсчет среднего количества попыток."""

import numpy as np

def random_predict(number:int=1) -> int:

    """рандомно угадываем число
    
    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return count

def score_game(random_predict) -> int:
    """
    За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    [extended_summary]

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__ == '__main__':
    # RUN
    score_game(random_predict)