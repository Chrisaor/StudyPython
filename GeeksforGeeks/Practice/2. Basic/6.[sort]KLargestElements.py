t = int(input())

for i in range(t):
    answer = []
    n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for j in range(int(n[1])):
        answer.append(max(arr))
        arr.remove(max(arr))
    print(" ".join(str(i) for i in answer))
