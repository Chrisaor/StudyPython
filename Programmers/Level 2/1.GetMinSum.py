def getMinSum(A,B):
    A.sort()
    B.sort()
    B.reverse()
    answer = 0
    print(A)
    print(B)
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer


print(getMinSum([1,2,1,2,5,6,], [3,4,2,1,3,6]))

'''<Clean Code>
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

print(getMinSum([1, 2], [3, 4]))
'''
