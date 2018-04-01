# def print_args(*args):
#     print('Positional argument tuple:', args)
#
#
# print_args(3,2,1, 'wait', 'uh..')
#
#
# def print_more(required1, required2, *args):
#     print('Need this one:', required1)
#     print('Need this one too:', required2)
#     print('All the rest:' , args)
#
# print_more('cap','gloves', 'scarf','monocle')
# 4.7.5
# def print_kwargs(**kwargs):
#     print('Keyword arguments:', kwargs)
#
# print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
# 4.7.7
# def answer():
#     print(42)
#
# answer()
#
# def run_somthing(func):
#     func()
#
# run_somthing(answer)
#
# print(type(run_somthing))

# def add_args(arg1, arg2):
#     print(arg1+arg2)
# # add_args(1,2)
#
# def run_somthing_with_args(func, arg1, arg2):
#     func(arg1, arg2)
#
# run_somthing_with_args(add_args,1,5)

# def sum_args(*args):
#     return sum(args)
#
# print(sum_args(1,2,3,4))
#
# def run_with_positional_args(func, *args):
#     return func(*args)
#
# print(run_with_positional_args(sum_args, 1,2,3,4))

# 4.7.8 내부 함수

# def outer(a,b):
#     def inner(c,d):
#         return c+d
#     return inner(a,b)
#
# print(outer(4,7))

# def knights(saying):
#     def inner(quote):
#         return "We are the knights who say: '%s'" % quote
#     return inner(saying)
#
# # print(knights('Ni'))
# a = knights('Ni')
#
# print(a)
# 4.7.9 클로져

# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s' " % saying
#     return inner2
#
# a = knights2('Duck')
# b = knights2('Hasenpfeffer')
# print(a)
# print(b)
# print(a())
# print(b())

# 4.9 데코레이터

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a,b):
    return a+b

# 수동으로 추가하기
# cooler_addints = document_it(add_ints)
# cooler_addints(3,5)

# 데코레이터로 추가
# @document_it
# def add_ints(a,b):
#     return a+b
#
# add_ints(3,5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a,b):
    return a+b

add_ints(3,5)
