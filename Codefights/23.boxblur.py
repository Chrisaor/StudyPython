import math

def boxBlur(image):
    temp1 = list()
    temp2 = list()
    temp3 = list()
    temp4 = list()
    result = list()
    answer = list()
    image_sum = 0

    for i in range(len(image)):
        for j in range(len(image)):
            for k in range(j, 3+j):
                # print(i,j,k)
                image_sum += image[i][k]
            temp1.append(image_sum)
            image_sum = 0
            # print('temp1',temp1)
            if 3+j >= len(image[0]) or j >= len(image)-1:
                temp2.append(temp1)
                temp1 = list()
                # print('append')
                break;
    # print(temp2)
    for i in range(len(temp2)):
        for j in range(len(temp2)):
            for k in range(i,i+3):
                # print(i,k,j)
                if k >= len(temp2) or j >= len(temp2[0]):
                    temp3 = list()
                    # print('break')
                    break;
                else:
                    temp3.append(temp2[k][j])
                    # print(temp3)
                    if len(temp3) == 3:
                        result.append(sum(temp3)//9)
                        temp3 = list()
                        # print('append')

        if i >= len(temp2[0])-1:
            break;
    if len(image[0]) == len(image):
        n_matrix = math.sqrt(len(result))
    else:
        n_matrix = len(result)
    # print(n_matrix)
    # print(result)
    for i in range(len(result)):
        temp4.append(result[i])
        # print(i%n_matrix)
        if i % n_matrix == n_matrix-1:
            answer.append(temp4)
            temp4 = list()
    # print(temp4)
    return answer

# 00 10 20
# 01 11 21
# 02 12 22
#
# 10 20 30
# 11 21 31
# 12 22 32
#
# 20 30 40
# 21 31 41
# 22 32 42
image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

#
# 11 5 4
# 13 10 9
# 23 25 21
# 7 6 11
# 10 6 8


# 11 5
# 13 10
# 23 25
# 7 6

#
print(boxBlur(image))
