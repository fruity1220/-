num = int(input())
hansu = 0

for i in range(1, num+1):
    if i <= 99:
        hansu += 1
    else:
        num1 = list(map(int, str(i)))
        if num1[0] - num1[1] == num1[1] - num1[2]:
            hansu += 1
print(hansu)