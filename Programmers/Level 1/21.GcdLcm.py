def gcdlcm(a, b):
    answer = []
    x = a
    y = b
    while y != 0:
        (x, y) = (y, x % y)
    answer = [x, int(a*b/x)]
    return answer

print(gcdlcm(128,8))

'''<Clean Code>
def gcdlcm(a, b):
    for i in range(a):
        if a%(a-i)+b%(a-i) == 0:
            return [a-i, a*b/(a-i)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))
'''
