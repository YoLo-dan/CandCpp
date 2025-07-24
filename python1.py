#2025/7/24 python判断语句
a = float(input())
b = float(input())
#关键 ： ①后面要有:号 ②一般要缩进四个字符
if a >= b:
    print("%.2f >= %.2f is right ! " % (a,b))
    print("%.2f 比 %.2f 大 %.2f ! " % (a,b,a-b))
else:
    print("%.2f >= %.2f is wrong ! " % (a,b))
    print("%.2f 比 %.2f 小 %.2f ! " % (a,b,b-a))
print("hello world ! ")


