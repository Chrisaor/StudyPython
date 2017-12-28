def Jaden_Case(s):
    strList = s.lower().split(" ")
    Jaden = ""
    for i in strList:
        Jaden += i[0].upper() + i[1:]
        if i != strList[-1]:
            Jaden += " "
    return Jaden



print(Jaden_Case("3people unFollowed me for the last week"))

'''<Clean Code>
def Jaden_Case(s):
    # 함수를 완성하세요
    s.lower()
    return s.title()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
'''
