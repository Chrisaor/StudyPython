
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];


emptyMatrix = [0 for x in range(len(b))]
result = [ emptyMatrix for y in range(len(b))]

print(result)
# #
# result = [[0,0], [0,0]]

print(result)
for i in range(len(b)):
    for j in range(len(b)):
        for k in range(len(b)):
            # print(a[i][k],b[k][j])
            print(result[i][j])
            result[i][j] += a[i][k] * b[k][j]
print(result)
