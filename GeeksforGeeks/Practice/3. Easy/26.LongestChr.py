def longest_dchr(str1):
    temp = list()
    result = list()
    str1_list = list(str1)
    if len(set(str1_list)) == len(str1_list):
        return len(str1_list)
    for i in range(len(str1_list)):
        if str1[i] in temp:
            result.append(len(temp))
            print(result)
            temp = temp[temp.index(str1[i])+1:]
            temp.append(str1[i])
            print(temp)
        else:
            temp.append(str1_list[i])
            print(temp)
    result.append(len(temp))
    return max(result) if not len(result)==0 else 0

# t = int(input())
# for i in range(t):
#     str1 = input()
str1 = 'okmnijnhbtgv'
print(longest_dchr(str1))
