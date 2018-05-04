from itertools import permutations

def four_elements(arr, n):
    perm = permutations(arr,4)
    for i in perm:
        if sum(i) == n:
            return 1
    return 0

t = int(input())
for i in range(t):
    N = input()
    arr = list(map(int, input().split()))
    n = int(input())
    print(four_elements(arr,n))
