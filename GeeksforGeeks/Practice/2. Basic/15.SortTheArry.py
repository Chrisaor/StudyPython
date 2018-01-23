t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sortedarr = sorted(arr)
    answer = ' '.join(map(str, sortedarr))
    print(answer)
