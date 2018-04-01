def longest_consecutive(num):
    temp = list()
    cnt = 0
    while num > 0:
        if num % 2 == 1:
            cnt += 1
        else:
            temp.append(cnt)
            cnt = 0
        num = (num >> 1)
    temp.append(cnt)
    return max(temp)

t = int(input())
for i in range(t):
    num = int(input())
    print(longest_consecutive(num))
