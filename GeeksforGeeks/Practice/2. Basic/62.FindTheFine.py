def find_the_fine(date, num, fine):
    sum_fine = 0
    for i in range(len(num)):
        if date % 2 == 0:
            if num[i] % 2 == 1:
                sum_fine += fine[i]
        else:
            if num[i] % 2 == 0:
                sum_fine += fine[i]
    return sum_fine

t = int(input())
for i in range(t):
    N = list(map(int, input().split()))
    date = N[1]
    num = list(map(int, input().split()))
    fine = list(map(int, input().split()))
    print(find_the_fine(date,num,fine))
