def non_repeating_chr(str):
    list1 = list(str)
    for i in range(len(list1)):
        if list1.count(list1[i]) == 1:
            return list1[i]
    return -1


t = int(input())
for i in range(t):
    n = int(input())
    str = input()
    print(non_repeating_chr(str))
