1.
a=10
b=10
c=20
r = (a + b * ( c / 2 ))
print (r)

2.
a=31232
b=21533
r =(a**2+b**2)%2
print (r)

3.
a=10
b=10
c=10
r=( a + b ) // 12 * c %4 + b
print (r)

4.
a=10
b=10
c=10
r=(a -b*c)//(a+b)%c
print (r)

5.
import math
a=10
b=20
c=30
r= math.fabs(a-b)//(a + b)**3-math.cos(c)
print (round (r,2))
#
6.
import math
a=10
b=20
c=30
r=(math.log(1+c)//-b)**4+a
print (r)


7.
def EU_change_USA_data(date):
    S1 = date[:3]
    S2 = date[3:6]
    S3 = date[6:]
    result=S2+S1+S3
    return result, date

result, original = EU_change_USA_data("12.21.2016")
print(result, original)

8.
import math
def in_middle(string1, string2):
    result=string1[:math.floor(len(string1)/2)] + string2 + string1[math.floor(len(string1)/2):]
    return result
string1='aaaa'
string2='bb'
result1=in_middle(string1,string2)
result=in_middle(result1,string1)
print (result)


9.
import math
def grad2rad(angle):
    result=math.radians(angle)
    return result
angle1 = grad2rad(60)
result1 = math.cos(angle1)
print(math.cos(result1),'\n%s' %angle1)
angle2 = grad2rad(45)
result2 = math.cos(angle2)
print(math.cos(result2),'\n%s' %angle2)
angle3 = grad2rad(40)
result3 = math.cos(angle3)
print(math.cos(result3),'\n%s' %angle3)


10.
a = input("Введите трехзначное число: ")
def sum_num (a):
    a = int(a)
    num1 = a % 10
    num2 = a % 100 // 10
    num3 = a // 100
    result=num1+num2+num3
    return result
result=sum_num(a)
print("Сумма цифр числа:",result)


12.
num = int (23)
def nechetnoe_chislo(num):
    result = (num % 2) != 0
    return result
result=nechetnoe_chislo(num)
print (result)
#
17.
def fac(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac
result= (fac(5))
print (result)


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n
result= (fac(10))
print (result)


Поиск факториала с помощью цикла ()
n = input("Факториал числа ")
n = int(n)
fac = 1
i = 0
while i < n:
     i += 1
     fac = fac * i
print ("равен",fac)


19.
import math
n = int(100)
lst=[]
for i in range(2, n+1):
    for a in lst:
        if a > int((math.sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % a == 0):
            break
    else:
        lst.append(i)
print (lst)


22.
import random
def chooose ():
    x=random.randint(1,10)
    print(x)
    while True:
        y=input("Number:")
        if int(y)> 10:
            print("Казна полна, Милорд!")
            continue
        if int(y)<- 1:
            print("Казна пуста, Милорд!")
            continue
        if int (y)<x:
           print("Нужно больше золота, Милорд!")
        elif int (y)>x:
            print("Нужно меньше, Милорд!")
        else:
            print("За Короля!!!")
            break
chooose()



