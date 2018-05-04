def uncommon_chr(str1, str2):
    temp = list()
    for i in list(str1):
        if i not in list(str2):
            temp.append(i)
    for j in list(str2):
        if j not in list(str1):
            temp.append(j)

    return ''.join(sorted(set(temp)))


t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    print(uncommon_chr(str1,str2))
