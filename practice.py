

# grade = {'pey':10, 'jullien':99}
# print(grade['pey'])
# print(grade['jullien'])
#
# # print(grade[0]) key에러 발생
#
# print(grade.keys())
# print(grade.values())

# print(dir(grade.values))

# for k in grade.keys():
#     print(k)
#
# for v in grade.values():
#     print(v)

# print(list(grade.keys()))
#
# print(grade.get('pey'))

# print(grade.items())
# print('pey' in grade)
#
# for i in grade.items():
#     print(i)


class FileOwners:

    @staticmethod
    def group_by_owners(files):

        owner_dict = dict()
        owner_book = list()
        for key, value in files.items():
            temp = [value, key]
            owner_book.append(temp)

        for i in owner_book:
            if i[0] not in owner_dict:
                owner_dict[i[0]] = [i[1]]
            else:
                owner_dict[i[0]].append(i[1])
        return owner_dict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
#
#
# dict1 = {
# '1': 'one',
# '2': 'two'
# }
#
# if '2' in dict1:
#     print('exist')
# else:
#     print('not exist')


class Palindrome:

    @staticmethod
    def is_palindrome(word):
        l_word = word.lower()

        if len(word)%2 ==0:
            if l_word[:len(word)//2] == l_word[:len(word)//2-1:-1]:
                print(l_word[:len(word)//2])
                print(l_word[:len(word)//2-1:-1])
                return True
            else:
                print(l_word[:len(word)//2])
                print(l_word[:len(word)//2-1:-1])
                return False
        else:
            if l_word[:len(word)//2] == l_word[:len(word)//2:-1]:
                print(l_word[:len(word)//2])
                print(l_word[:len(word)//2:-1])
                return True
            else:
                print(l_word[:len(word)//2])
                print(l_word[:len(word)//2:-1])
                return False


print(Palindrome.is_palindrome('Delseled'))
