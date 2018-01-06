from itertools import permutations


def allPermutations(str):
    answer = []
    permList = permutations(str)
    for perm in list(permList):
        answer.append(''.join(perm))
    return ' '.join(answer)


t = int(input())

for i in range(t):
    str1 = input()
    strList = []
    for j in range(len(str1)):
        strList.append(str1[j])
    strList.sort()
    str2 = ''.join(strList)
    print(allPermutations(str2))
