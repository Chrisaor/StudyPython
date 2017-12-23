def strToInt(str):
    return int(str)
    
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));

'''<다른 풀이>
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[함:-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));
'''