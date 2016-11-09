import math
import random
simple_list=[0]*2
def print_list(lst):
    for i in range(0,len(lst)):
         print("Element of the list is equal to", lst[i])
#
def fill_random_list(lst):
    for i in range(0, len(lst)):
        random_num = random.randint(0, 100)
        lst[i] = random_num
def find_average_from_list(lst):
    s=lst[0]
    for i in lst:
        s += i
    return s/len(lst)
fill_random_list(simple_list)
print_list(simple_list)
result = find_average_from_list(simple_list)
print (result)