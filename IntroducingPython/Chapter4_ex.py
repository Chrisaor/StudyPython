# 4.1

# guess_me = 7
# if guess_me < 7:
#     print('too low')
# elif guess_me > 7:
#     print('too high')
# else:
#     print('just right')

# 4.2

# guess_me = 7
# start = 1
#
# while start:
#     if start < guess_me:
#         print('too low')
#     elif start == guess_me:
#         print('found it!')
#     else:
#         print('oops')
#         break;
#     start += 1

# 4.3

# list1 = [i for i in range(4)][::-1]
# print(list1)

# 4.4
#
# list1 = [i for i in range(10) if i%2 == 0]
# print(list1)

# 4.5
#
# dic1 = {i:i**2 for i in range(10) if i%2 == 0}
# print(dic1)

# 4.6

# set1 = {i for i in range(10) if i % 2}
# print(set1)

# 4.7

# generator = ('Got ' + str(i) for i in range(10))
# print(generator)
# for i in generator:
#     print(i)

# 4.8
#
# def good():
#     list1 = ['Harry', 'Ron', 'Hermione']
#     print(list1)
# good()

# 4.9
#
# def get_odds(first=1, last=10, step=2):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# for index, i in enumerate(get_odds()):
#     if index == 2:
#         print(i)
#

# 4.10

# def test(func):
#     def new_function(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return new_function
#
# @test
# def loop1(n):
#     print(sum(range(n)))
#
#
# loop1(10)

# 4.11

# class OopsException(Exception):
#     pass
#
# try:
#     raise OopsException('panic')
# except OopsException as exc:
#     print('Caught an oops')

# 4.12
#
# movies = dict()
# titles = ['Creature of Habit', 'Crewel Fate']
# plots = ['A nun turns into a monster', 'A haunted yarn shop']
# for key, item in zip(titles, plots):
#     movies[key] = item
#
# print(movies)
