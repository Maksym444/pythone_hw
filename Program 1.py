




import math
a = float(int(5))
b = float(int(4))
c = float(int(2))
def discr_2(discr):
    result=b ** 2 - 4 * a * c
    return result
x=discr_2(discr_2)
print("Дискриминант D = %.2f" % discr_2(discr_2))
if x > 0:
    x1 = (-b + math.sqrt(discr_2)) / (2 * a)
    x2 = (-b - math.sqrt(discr_2)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr_2 == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")