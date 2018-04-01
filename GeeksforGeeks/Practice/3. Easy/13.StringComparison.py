import string
def string_comparison(str1, str2):

    str_ascii = string.ascii_lowercase
    str_list = [' ']

    for i in str_ascii:
        if i == 'n':
            str_list.append(i)
            str_list.append('ng')
        else:
            str_list.append(i)
    print(str_list)

    str1_cnt = 0
    str2_cnt = 0
    str1_list = list()
    str2_list = list()

    for i in range(len(str1)):
        if str1[i] == 'n' and i < len(str1)-1:
            if str1[i+1] == 'g':
                str1_list.append('ng')
            else:
                str1_list.append('n')
        elif str1[i] == 'g' and str1[i-1] == 'n':
            continue
        else:
            str1_list.append(str1[i])

    for i in range(len(str2)):
        if str2[i] == 'n' and i < len(str2)-1:
            if str2[i+1] == 'g':
                str2_list.append('ng')
            else:
                str2_list.append('n')
        elif str2[i] == 'g' and str2[i-1] == 'n':
            continue
        else:
            str2_list.append(str2[i])

    if len(str1_list) > len(str2_list):
        str2_list += [' '] * (len(str1_list) - len(str2_list))
    else:
        str1_list += [' '] * (len(str2_list) - len(str2_list))
    for a, b in zip(str1_list, str2_list):
        str1_cnt += str_list.index(a)
        str2_cnt += str_list.index(b)
    if str1_cnt > str2_cnt:
        return 1
    elif str2_cnt > str1_cnt:
        return -1
    return 0


t = int(input())
for i in range(t):
    str_input = list(input().split(' '))
    str1 = str_input[0]
    str2 = str_input[1]
    print(string_comparison(str1, str2))
