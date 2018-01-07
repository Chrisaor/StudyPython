def swapNibbles(n):
    lowerNib = n&15
    upperNib = n >> 4
    answer = lowerNib*16 + upperNib
    return answer



t = int(input())
for i in range(t):
    n = int(input())
    print(swapNibbles(n))
