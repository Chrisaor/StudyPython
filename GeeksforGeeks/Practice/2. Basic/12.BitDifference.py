def bitDiff(A,B):
    bitA = bin(A)[2:]
    bitB = bin(B)[2:]
    bitLen = abs(len(bitA)-len(bitB))
    answer = 0
    if len(bitB) >= len(bitA):
        bitA = '0'*bitLen + bitA
    else:
        bitB = '0'*bitLen + bitB
    for i in range(len(bitA)):
        if bitA[i] != bitB[i]:
            answer += 1
    return answer




t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    print(bitDiff(n[0],n[1]))
