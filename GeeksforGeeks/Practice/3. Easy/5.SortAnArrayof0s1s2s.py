def sortArr012(arr):
    sortedarr = sorted(arr)
    answer = ' '.join(map(str, sortedarr))
    return answer

t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(sortArr012(arr))
