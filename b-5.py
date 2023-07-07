from typing import List


def cal_total(numbers: List[int]) -> int:
    total_data = 0
    for i in numbers:
        total_data += i
    return total_data


def cal_max(numbers: List[int]) -> int:
    max_data = 0
    for i in numbers:
        if max_data < i:
            max_data = i
    return max_data


def cal_min(numbers: List[int]) -> int:
    min_data = numbers[0]
    for i in numbers:
        if min_data > i:
            min_data = i
    return min_data


def cal_avg(numbers: List[int]) -> int:
    avg_data = cal_total(numbers) // len(numbers)
    return avg_data


input_data = input("データを入力してください(スペース区切り) > ")  # input_data = "5 8 13 21"

data = input_data.split(" ")  # ["5","8","13","21"]

numbers = []
for i in data:
    int_number = int(i)
    numbers.append(int_number)

total = cal_total(numbers)
max = cal_max(numbers)
min = cal_min(numbers)
avg = cal_avg(numbers)

print(f"合計値:{total}")
print(f"最大値:{max}")
print(f"最小値:{min}")
print(f"平均値:{avg}")
