def closet_number(n,m):
    answer = 0
    if n*m == 0:
        return 0
    elif n*m > 0:
        if (n/m - n//m) >= 0.5:
            answer = (m * (n//m+1))
        else:
            answer = (m * (n//m))
    else:
        if abs((n/m - (n//m+1))) >= 0.5:
            answer = (m * (n//m))
        else:
            answer = (m * (n//m+1))
    return answer

# t = int(input())
# for i in range(t):
#     num = list(map(int, input().split()))
#     n = num[0]
#     m = num[1]
#     print(closet_number(n,m))

print(closet_number(-19, 5))
