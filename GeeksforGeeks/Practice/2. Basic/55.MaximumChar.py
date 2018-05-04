def maximum_char(char1):
    count_list = list()
    temp = list()
    for i in char1:
        count_list.append(char1.count(i))

    max_count = max(count_list)
    for i in char1:
        if char1.count(i) == max_count:
            temp.append(i)
    return sorted(temp)[0]

t = int(input())
for i in range(t):
    char1 = input()
    char1 = list(char1)
    print(maximum_char(char1))
