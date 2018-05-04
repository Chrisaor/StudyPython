def spirally_matrix(matrix):
    N = len(matrix)
    answer = []
    for i in range(N):
        # print('i : ',i)
        answer.append(matrix[i][i:len(range(N))-i])
        # print(answer)
        if N-1-i == 2:
            answer.append(matrix[i+1][N-i-1:N-i-3:-1])
            result = list()
            for i in range(len(answer)):
                result += answer[i]
            result = list(map(str, result))
            return ' '.join(result)
        else:
            for j in range(i+1, N-1-i):
                # print('j : ',j)
                answer.append(matrix[j][-1-i::])
                # print(answer)
            answer.append(matrix[-1-i][len(range(N))-i::-1])
            # print(answer)
            for k in reversed(range(i+1, N-1-i)):
                answer.append([matrix[k][i]])
                # print(answer)


    return -1


matrix = [
 [1,2,3,4,5,6],
 [6,7,8,9,10,16],
 [11,12,13,14,30],
 [15,16,17,18,31],
 [19,20,21,22,32],
 [33,34,35,36,37,38]
]
# t = int(input())
# for i in range(t):
#     matrix = list()
#     for j in range(4):
#         mat = list(map(str,input().split()))
#         matrix.append(mat)
print(spirally_matrix(matrix))
