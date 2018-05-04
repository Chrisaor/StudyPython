def twice_counter(list1):
    temp = list()
    cnt = 0
    for i in range(len(list1)):
        if list1.count(list1[i]) == 2:
            temp.append(list1[i])
    return len(set(temp))

t = int(input())
for i in range(t):
    n = input()
    list1 = list(input().split(' '))
    print(twice_counter(list1))
