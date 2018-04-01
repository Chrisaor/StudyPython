def remove_chr(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    result = list()
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] not in list2:
                result.append(list1[i])
                break;


    return ''.join(result)

t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    print(remove_chr(str1, str2))
