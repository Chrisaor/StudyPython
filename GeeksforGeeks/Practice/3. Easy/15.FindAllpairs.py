def find_all_pairs(A,B,x):
    temp = list()
    answer = list()
    for j in range(len(B)):
        for i in range(len(A)):
            if (A[i]+B[j]) == x:
                temp.append(A[i])
                temp.append(B[j])
                answer.append(temp)
                temp = list()
    if len(answer) == 0:
        return -1
    else:
        answer = sorted(answer)
        for i in range(len(answer)):
            answer[i] = list(map(str, answer[i]))
        return ', '.join([' '.join(i) for i in answer])


# t = int(input())
# for i in range(t):
#     N = list(map(int, input().split()))
#     x = N[2]
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     print(find_all_pairs(A,B,x))
A_str = "-1 5 -8 -10 11 -16 20 -22 -26 -28 -30 -36 40 43 -44 -46 61 -65 68 78 -99"
# A = [-1, -2, 4, -6, 5, 7]
B_str = "0 -1 4 5 6 7 9 10 11 -12 -13 -18 19 20 -21 22 -24 26 -27 28 -30 31 33 -36 -37 39 40 -42 45 48 50 -52 -55 -56 58 59 -60 62 63 -66 -67 68 69 71 72 -73 76 -79 -81 -84 87 90 -94 95 96 99"
# B = [6, 3, 4, 0]
x = 52
A = list(map(int, A_str.split()))
B = list(map(int, B_str.split()))
print(find_all_pairs(A,B,x))
