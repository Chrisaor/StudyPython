def numPY(s):
    pNum = 0
    yNum = 0
    for i in range(len(s)):
        if s[i] == "p" or s[i] =="P":
            pNum += 1
        elif s[i] == "y" or s[i] =="Y":
            yNum += 1
    if pNum == yNum:
        return True
    else:
        return False

print(numPY("pPoooyY"))
print( numPY("Pyy") )

'''<Clean Code>
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
'''
