def transform_the_array(arr):
    rm_zero = list()
    trans_arr = list()
    zeros = 0
    for i in arr:
        if i == 0:
            zeros += 1
        else:
            rm_zero.append(i)

    for i in range(len(rm_zero)):
        if i == 0:
            trans_arr.append(rm_zero[0])
        elif rm_zero[i] == trans_arr[-1]:
            trans_arr[-1] = trans_arr[-1]*2
            zeros += 1
        else:
            trans_arr.append(rm_zero[i])

    answer = trans_arr + [0]*zeros
    return ' '.join(map(str, answer))

t = int(input())
for i in range(t):
    n = input()
    arr = list(map(int, input().split()))
    print(transform_the_array(arr))
