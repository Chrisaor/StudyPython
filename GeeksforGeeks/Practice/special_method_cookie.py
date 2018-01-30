class Cookie:
    '나는 cookie를 만드는(정의하는) 기계(클래스)'
    def __init__(self, name, weight): #인스턴트가 생성될 때 자동으로 실행되는 함수
        self.name = name  # 받아온 name을 속성의 값으로 이용
        self.weight = weight # 받아온 weight을 속성의 값으로 이용


    # def create(name, weight):  create 이 함수는 이제 쓸모가 없게 된다.
    #     cookie = Cookie()      왜냐하면 __init__에서 name, weight를 받을 수 있으니까
    #     cookie.name = name
    #     cookie.weight = weight
    #     return cookie
    def __str__(self): # 인스턴스 자체를 출력할때 포맷을 설정할 수 있음
        return "{} (몸무게 {}g)".format(self.name, self.weight)


    def add(self): # 쿠키의 중량을 추가하는 메소드
        self.weight += 1  # 쿠키의 weight속성에 1g추가
        print('{}의 중량이 {}g 가 되었습니다.'.format(self.name, self.weight))
        #출력
    def sub(self):
        self.weight -= 1
        print('{}의 중량이 {}g 가 되었습니다'.format(self.name, self.weight))

cookie = Cookie('초코칩', 300) # 초코칩과, 300g중량의 쿠키 인스턴스 생성
print(cookie)
print(cookie.name)  # 인스턴스
print(cookie.weight)
