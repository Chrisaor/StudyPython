def max_sum_without_adjacents():
    return


arr = [3, 2, 5, 10, 7]
nominate = list()
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if j-idx == 1:
            continue
        else:
            cnt += arr[j]
            idx += 1
    nominate.append(cnt)

print(nominate)


#
# 3 5 7 = 15
# 3 10 = 13
# 2 10 = 12
# 2 7 = 9
