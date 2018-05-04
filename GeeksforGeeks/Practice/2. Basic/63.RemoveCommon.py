def remove_common(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    temp = list()
    for i in list1:
        if i not in list2:
            temp.append(i)
    for i in list2:
        if i not in list1:
            temp.append(i)
    if len(temp) != 0:
        return ''.join(temp)
    else:
        return -1

t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    print(remove_common(str1, str2))
