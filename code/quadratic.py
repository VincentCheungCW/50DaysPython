# 求一元二次方程的平方根：定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。

import math


def quadratic(a, b, c):
    delta = pow(b, 2) - 4 * a * c  # 声明一元二次方程判别式,pow(a, b)函数表示a的b次方

    if delta < 0:
        return 'no solution'  # 无解
    elif a == 0:  # 注意必须用等号==，而不是=
        return 'insignificance'  # 无意义
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print('quadratic(1,4,4)=', quadratic(1, 4, 4))  # delta==0,得到两个相等的根
print('quadratic(0,3,2)=', quadratic(0, 2, 2))  # a==0,解出来无意义(insignificance)
print('quadratic(3,1,4)=', quadratic(3, 1, 4))  # 不存在根(no solution)

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
