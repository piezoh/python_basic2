import random
from typing import List


def roll_dice(side: int, times: int) -> List[int]:
    result = []  # 空のリストを用意

    for i in range(times):
        dice = random.randint(1, side)
        result.append(dice)  # resultのりすとにdiceの値を要素として追加
    return result


s = int(input("サイコロの面の数は?:"))
t = int(input("何回振りますか?: "))

print(roll_dice(side=s, times=t))
