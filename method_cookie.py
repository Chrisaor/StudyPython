class Cookie:
    '나는 cookie를 만드는(정의하는) 기계(클래스)'

    def create(name, weight): #쿠키를 만드는 메소드! 만들기 버튼
        cookie = Cookie()  #우선 인스턴스를 만든다
        cookie.name = name
        #쿠키의 이름 속성은 함수의 name parameter로 받아온 이름으로 지정
        cookie.weight = weight
        #쿠키의 맛 속성은 함수의 flavor parameter로 받아온 이름으로 지정
        return cookie  #만들어진 인스턴스를 반환!

    def add(self): # 쿠키의 중량을 추가하는 메소드
        self.weight += 1  # 쿠키의 weight속성에 1g추가
        print('{}의 중량이 {}g 가 되었습니다.'.format(self.name, self.weight))
        #출력
    def sub(self):
        self.weight -= 1
        print('{}의 중량이 {}g 가 되었습니다'.format(self.name, self.weight))


cookie = Cookie.create('초코칩', 300) # create_cookie함수에 의한 cookie인스턴스 생성!
cookie.add() #쿠키 인스턴스의 add속성을 호출
cookie.sub()
