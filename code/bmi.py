while True:
    print("BMI计算器")
    height = input("请输入你的身高（米）：")
    weight = input("请输入你的体重（千克）：")

    bmi = float(weight) / (float(height) * float(height))
    print("你的BMI指数：" + str(bmi.__round__(2)))

    if bmi < 18.5:
        print("过轻")
    elif 18.5 <= bmi < 25:
        print("正常")
    elif 25 <= bmi < 28:
        print("过重")
    elif 28 <= bmi < 32:
        print("肥胖")
    elif 32 <= bmi:
        print("严重肥胖")

    print("\n")




