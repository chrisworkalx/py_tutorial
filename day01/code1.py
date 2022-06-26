"""
第一个demo

"""


import math
# a = 113


# 113 <class 'int'>
# print(a, type(a))


# print(f'{a}', type(a))  # 113 <class 'int'>
# print(f'a', type(a))  # a <class 'int'>


# 计算一个圆的面积

# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius ** 2


# .2f表示保留两位小数
# print(f'圆的周长是: {perimeter:.2f}')
# print(f'圆的面积是: {area:.2f}')


# 判断闰年规则
# 如何判断闰年的规则
# 年份是4的倍数但不是100的倍数，或者是400的倍数


# year = int(input('请输入年份: '))

# print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


# 如何判断一个三角形
# 边长a, 边长b, 边长c
# 如果a, b, c都大于0，且a + b > c, a + c > b, b + c > a

# a = float(input('请输入边长a: '))
# b = float(input('请输入边长b: '))
# c = float(input('请输入边长c: '))
# print(a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a)


# 英寸转厘米
# 输入英寸数，输出厘米数
# 1英寸 = 2.54厘米
x = float(input('请输入英寸数: '))
print(f'{x}英寸 = {x * 2.54:.2f}厘米')
