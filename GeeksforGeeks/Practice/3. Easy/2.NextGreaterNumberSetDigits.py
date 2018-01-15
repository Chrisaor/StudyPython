from itertools import permutations

def nextGreater(n):
    sortedStr = sorted(n)
    strOder = []
    idx = 0
    permList = permutations(sortedStr)
    for perm in list(permList):
        element = ''.join(perm)
        if element not in strOder:
            strOder.append(element)
    idx = strOder.index(n) + 1
    try :
        answer = strOder[idx]
    except IndexError:
        return "not possible"
    return answer

t = int(input())
for i in range(t):
    n = input()
    print(nextGreater(n))
