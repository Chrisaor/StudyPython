def columName(n):
    answer = ""
    while n:
        letter = chr(((n-1) % 26) + 65)
        answer += letter
        if (n % 26) == 0:
            n = n - 1
        n = n //26

    return answer[::-1]

t = int(input())
for i in range(t):
    n = int(input())
    print(columName(n))
