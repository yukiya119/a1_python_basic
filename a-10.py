import random

def dice():
    number = [1, 2, 3, 4, 5, 6]
    result = random.choice(number)
    return result

print(dice())  # 1から6の整数をランダムに出力する
