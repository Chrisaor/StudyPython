def keyPair(n, x, list2):
    for i in range(n):
        temp = 0
        for j in range(i+1,n):
            temp = list2[i] + list2[j]
            if temp == x:
                return "Yes"

    return "No"


t = int(input())
for i in range(t):
    size = list(map(int, input().split()))
    n = size[0]
    x = size[1]
    list2 = sorted(list(map(int, input().split())))
    print(keyPair(n,x,list2))
