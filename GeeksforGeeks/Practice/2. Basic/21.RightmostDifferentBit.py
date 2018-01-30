def rightmost_different_bit(m,n):
    xor_result = bin(m^n)[2:]
    for i in range(1,len(xor_result)+1):
        if xor_result[-i] == '1':
            return i



t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    m = arr[0]
    n = arr[1]
    print(rightmost_different_bit(m,n))
