def nlcm(num):
    for i in range(len(num)-1):
        num.sort()
        num.reverse()
        a = num[0]
        b = num[1]
        x = a
        y = b
        while y != 0:
            (x, y) = (y, x % y)
        num.append(int(a*b/x))
        num = num[2:]
    return num[0]

print(nlcm([2,6,8,14]))


'''<Clean Code>
from fractions import gcd

def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer
'''
