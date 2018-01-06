#List of Integers
numbers = [1, 3, 4, 2]
numbers. sort()
print(numbers)

#List of Floating point numbers
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]
decimalnumber.sort()
print(decimalnumber)

#List of strings
words = ["Geeks", "For", "Geeks"]
words.sort()
print(words)

'''
Syntax:

list_name.sort()  : ascending order
list_name.sort(reverse=True)  : descending order
list_name.sort(key = ..., reverse = ...)  : according to user's choice
'''
def sortSecond(val):
    return val[1]

list1 = [(1,2), (3,3), (1,1)]
list1.sort(key=sortSecond)
print(list1)

list1.sort(key=sortSecond, reverse =True)
print(list1)
