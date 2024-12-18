"""
Задачка1 сумма всех чисел

"""

# def sum_num(a):
#     am = 1
#     rez = 0
#     while int(am) <= int(a):
#         rez += am
#         am += 1
#         print(rez)
#     print(rez)
#
#
# try:
#     a = int(input())
#     sum_num(a)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


"""
Задачка 2 среднее число из массива
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.

"""

# def find_average(num):
#     if num:
#         return print(sum(num) / len(num))
#     else:
#         return print('0')

# # # return sum(num) / len(num) if num else 0
#
# # # from statistics import mean; find_average = lambda x: mean(x) if len(x) > 0 else 0


# number = input().split()
# int_num =[]
# for i in number:
#     int_num.append(int(i))
# print(int_num)
# find_average(int_num)


"""
Задача 3
Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3,
 "Boom" if it is divisible by 5, "BangBoom" if it divisible by 3 and 5, 
 and "Miss" if it isn't divisible by any of them. Note: Your program should only return one value

Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 --> Output: "Boom

"""
# def multiple(x):
#
#
#
#
#     if x % 3 == 0 and x % 5 == 0:
#         print(x / 3)
#         print(x / 5)
#         return print('BangBoom')
#     elif x % 3 == 0:
#         print(x / 3)
#         return print('Bang')
#     elif x % 5 == 0:
#         print(x / 3)
#         return print('Bang')
#     else:
#         print("не делится")
#         return print('Miss')
#
#
# number = int(input('Input number: '))
#
# multiple(number)

""" 
Задача 4

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.
"""


def are_you_playing_banjo(name):
    # Implement me!
    mes = " plays banjo" if name[0].lower() in 'r' else " does not play banjo"
    # mes = " plays banjo" if name[0] in 'rR' else " does not play banjo"  # alternative solution if case insensitivity is required
    return name + mes


usname = input('Input name: ')

print(are_you_playing_banjo(usname))

