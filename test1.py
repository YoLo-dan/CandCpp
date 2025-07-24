#2025/7/24 python判断语句
#关键 ： ①后面要有:号 ②一般要缩进四个字符
'''
a = float(input())
b = float(input())
if a >= b:
    print("%.2f >= %.2f is right ! " % (a,b))
    print("%.2f 比 %.2f 大 %.2f ! " % (a,b,a-b))
else:
    print("%.2f >= %.2f is wrong ! " % (a,b))
    print("%.2f 比 %.2f 小 %.2f ! " % (a,b,b-a))
print("hello world ! ")
'''
#输出绝对值
'''
a = int(input())
if a > 0:
    print(a)
else:
    print(-a)
'''
#输出最大值
'''
a , b = map(float,input().split())
if a >= b:
    print(a)
else:
    print(b)
'''
#输入三个数，输出最大的数
'''
a, b, c = map(float,input().split())
if a >= b:
    if a >= c:
        print("最大的数字是a，a = %.2f" % a)
    else:
        print("最大的数字是c，c = %.2f" % c)
else:
    if b >= c:
        print("最大的数字是b，b = %.2f" % b)
    else:
        print("最大的数字是c，c = %.2f" % c)
'''
'''
x = float(input())
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 60:
    print("C")
else:
    print("D")
'''

#判断闰年
'''
year = int(input())
if year % 100 == 0:
    print("%d是闰年 ! " % year)
else:
    if year % 4 == 0:
        print("%d是闰年 ! " % year)
    else:
        print("%d不是闰年！！！" % year)
'''
'''
status = int(input())

match status:
    case 400:
        print(400)
    case 401:
        print(401)
    case 402:
        print(402)
    case _:
        print("something went wrong")
'''
#某商店出售 5种零食，零食编号为 1∼5。
'''
x, y = map(float,input().split())
match x:
    case 1:
        X = 4 * y
    case 2:
        X = 4.5 * y
    case 3:
        X = 5.00 * y
    case 4:
        X = 2.00 * y
    case 5:
        X = 1.50 * y

print("Total: R$ %.2f" % X)
'''


#ABC 公司决定给员工加薪，加薪情况如下所示：
'''
x = float(input())

if x > 2000:
    y = 0.04
elif x > 1200.01:
    y = 0.07
elif x > 800.01:
    y = 0.1
elif x > 400.01:
    y = 0.12
else:
    y = 0.15
print("Novo salario: %.2f" % (x * (1 + y)))
print("Reajuste ganho: %.2f" % (x * y))
print("Em percentual: %d %%" % (y*100))
'''

#读取三个整数并按升序对它们进行排序。
'''
a, b, c = map(int,input().split())
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print(a)
print(b)
print(c)
print("\n")
if a < b:
    a,b = b,a
if a < c:
    a,c = c,a
if b < c:
    b,c = c,b
print(a)
print(b)
print(c)
'''























