number = 34

while True:
    print('猜数游戏Begin…')
    guess = int(input('输入数字: '))

    if guess == number:
        print('Bingo, 猜对了')
        # 运行到break语句将跳出循环
        break
    elif guess < number:
        print('小了')
    else:
        print('大了')

print('游戏结束')
