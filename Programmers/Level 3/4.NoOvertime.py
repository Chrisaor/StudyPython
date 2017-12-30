# def noOvertime(n, works):
#
#
#     return
#
#
#
#
# print(noOvertime(4, [4,3,3]))


n = 3
works = [4, 5, 2]
sumWorks = sum(works)
leftWorks = sumWorks - n
avg = int(leftWorks//len(works))
print(sumWorks-n)
for i in range(len(works)):
    works[i] = avg
