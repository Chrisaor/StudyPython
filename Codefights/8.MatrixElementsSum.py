def matrixElementsSum(matrix):
    sum_matrix = 0
    
    haunted_room = list()
    for i in range(0, len(matrix)):
        # print('i',i)
        for j in range(len(matrix[0])):
            # print('i',i, 'j',j)
            if matrix[i][j] == 0:
                haunted_room.append(j)
                # print(haunted_room)
        for k in range(len(matrix[0])):
            # print('i',i, 'j',j, 'k',k)
            if k not in haunted_room:
                sum_matrix += matrix[i][k]
                # print(sum_matrix)
    return sum_matrix

matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

print(matrixElementsSum(matrix))

# #
# print(matrix[0])
#
# print(sum(matrix[0]))
# print(len(matrix))
# sum_matrix = 0
# sum_matrix += sum(matrix[0])
# haunted_room = list()
#
# for i in range(1, len(matrix)):
#     print('i',i)
#     for j in range(len(matrix[0])):
#         print('i',i, 'j',j)
#         if matrix[i][j] == 0:
#             haunted_room.append(j)
#             print(haunted_room)
#     for k in range(len(matrix[0])):
#         print('i',i, 'j',j, 'k',k)
#         if k not in haunted_room:
#             sum_matrix += matrix[i][k]
#             print(sum_matrix)
