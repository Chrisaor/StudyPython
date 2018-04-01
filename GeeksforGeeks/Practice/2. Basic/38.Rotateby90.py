def rotate_by_90(N, arr):
    matrix = list()
    for i in range(N):
        matrix.append(arr[i*N:(i+1)*N])

    new_matrix = list()
    temp = list()

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(matrix[j][-i-1])
        new_matrix.append(temp)

    liner = list()
    for i in new_matrix:
        liner += i
    answer = ' '.join(map(str, liner))
    return answer

t = int(input())
for i in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    print(rotate_by_90(N,arr))
