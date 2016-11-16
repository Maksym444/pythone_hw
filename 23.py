#
<<<<<<< Updated upstream
def fill_random_list(lst):
    for i in range(0, len(lst)):
        random_num = random.randint(0, 100)
        lst[i] = random_num
def find_average_from_list(lst):
    s=0
    for i in lst:
        s += i
    return s/len(lst)
fill_random_list(simple_list)
print_list(simple_list)
result = find_average_from_list(simple_list)
print (result)



=======
# import random
# simple_list=[0]*2
# def print_list(lst):
#     for i in range(0,len(lst)):
#          print("Element of the list is equal to", lst[i])
#
# def fill_random_list(lst):
#     for i in range(0, len(lst)):
#         random_num = random.randint(0, 100)
#         lst[i] = random_num
# # def find_average_from_list(lst):
# #     s=0
# #     for i in lst:
# #         s += i
# #     return s/len(lst)
# fill_random_list(simple_list)
# print_list(simple_list)
# result = find_average_from_list(simple_list)
# print (result)
#



# import random
# def print_list(lst):
#     print("Element of the list is equal to", end=' ')
#     for i in lst:
#         print(i, end=' ')
#
# def find_average_from_list(lst):
#     s = 0
#     for number in lst:
#         s += number
#     return s/len(lst)
#
# rand_list = [random.randint(0, 100) for _ in range(10)]
# print_list(rand_list)
# result = find_average_from_list(rand_list)
# print('\n')
# print(result)

























































29.
import string
import random


def generate_password(pass_len=8):
    all_sym = string.ascii_letters + string.digits + '_'
    while True:
        password = ''
        lowercase = 0
        uppercase = 0
        ints = 0
        for i in range(pass_len):
            _ = all_sym[random.randint(0, len(all_sym)-1)]
            password += _
            if _ in string.ascii_lowercase:
                lowercase += 1
            elif _ in string.ascii_uppercase:
                uppercase += 1
            elif _ in string.digits:
                ints += 1
        if lowercase and uppercase and ints:
            return password


print(generate_password(8))
print(generate_password(8))
print(generate_password(8))
print(generate_password(8))
print(generate_password(8))
>>>>>>> Stashed changes
