# def menu(wine, entree, dessert='pudding'):
#     return {'wine':wine, 'entree':entree, 'dessert':dessert}
#
#
# print(menu('wine1', 'entree1','icecream'))


# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)
#
# buggy('a')
# buggy('b')
# buggy('c')
#
# def nonbuggy(arg, result=None):
#     if result is None:
#         result = []
#     result.append(arg)
#     print(result)

# def print_args(*args):
#     print('Positional argument tuple:', args)
#
# print(print_args(3,2,1,'wait!','uh..'))
#
# def print_more(req1, req2, *args):
#     print('Need this one:', req1)
#     print('Need this too', req2)
#     print('all the rest', args)
#
# print_more('cap','gloves','scarf','monocle')

def print_kwargs(**kwargs):
    print('Keyword arguments', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
