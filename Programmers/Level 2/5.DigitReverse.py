def digit_reverse(n):
    x = str(n)
    result = []
    for i in range(len(x)):
        result.append(int(x[i]))
    result.reverse()
    return result

print("결과 : {}".format(digit_reverse(12345)))


'''<Clean Code>
def digit_reverse(n):
    return [int(x) for x in str(n)][::-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));
'''
