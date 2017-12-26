def nextSqure(n):
    sqrt = n **(0.5)
    if int(sqrt) == sqrt:
        return (sqrt + 1)**2
    else:
        return "no"

print("결과 : {}".format(nextSqure(121)))

'''<Clean Code>
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
'''
