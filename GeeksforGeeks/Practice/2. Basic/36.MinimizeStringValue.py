import string

def minimize_string(str1, k):
    str_list = [i for i in str1]
    cnt_list = list()
    ascii_str = [i for i in string.ascii_lowercase]
    for i in ascii_str:
        if i in str1:
            cnt_list.append(str1.count(i))
    for i in range(k):
        if max(cnt_list) == 0:
            return 0
        else:
            cnt_list[cnt_list.index(max(cnt_list))] -= 1
    return sum([i**2 for i in cnt_list])

t = int(input())
for i in range(t):
    str1 = input()
    k = int(input())
    print(minimize_string(str1,k))
