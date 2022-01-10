"""Игра угадай число
компьютер сам загадывает и угадывает число"""

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

print(f'Количество попыток: {random_predict(10)}')