def hide_numbers(s):
    hide = ""
    for i in range(len(s[:-4])):
        hide += "*"

    s = hide + s[-4:]
    return s

print("결과 : " + hide_numbers('01033334444'))

'''<Clean Code>
def hide_numbers(s):
    return '*'*len(s[:-4]) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
'''
