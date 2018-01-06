def powerOf2(n):
    if n == 1:
        return print("YES")
    elif n == 0:
        return print("NO")
    else:
        while n // 2 != 0:
            if n % 2 != 0:
                return print("NO")
            else:
                n = n // 2
    return print("YES")

t = int(input())

for i in range(t):
    n = int(input())
    powerOf2(n)

'''<Clean Code>
for _ in range(int(input().strip())):
    n = int(input().strip())
    print((n==0 or n&(n-1)) and "NO" or "YES")
'''
