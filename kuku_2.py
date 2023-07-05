num_lines = int(input("行数を入力してください:"))
num_column = int(input("列数を入力してください:"))

for a in range(1, num_lines + 1):
    for b in range(1, num_column + 1):
        c = a * b
        print(c, end=" ")
    print("")
