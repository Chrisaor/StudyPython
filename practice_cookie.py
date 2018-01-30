class Cookie:
    '나는 cookie를 만드는(정의하는) 기계(클래스)'


# cookieA = Cookie() # 쿠키A는 쿠키의 인스턴스(쿠키 클래스로 부터 찍어나온 초코칩)
# cookieA.name = '초코칩' #쿠키A의 이름 속성은 초코칩
# cookieA.flavor = 'chocolate' #쿠키A의 맛 속성은 chocolate

#이 코드를 새로운 쿠키를 만들 때마다 매번 반복해서 써야한다면 번거롭다.
#쿠키를 찍어내는 함수를 만들어보자

def create_cookie(name, weight):
    cookie = Cookie()  #우선 인스턴스를 만든다
    cookie.name = name
    #쿠키의 이름 속성은 함수의 name parameter로 받아온 이름으로 지정
    cookie.weight = weight
    #쿠키의 맛 속성은 함수의 flavor parameter로 받아온 이름으로 지정
    return cookie  #만들어진 인스턴스를 반환!


Cookie.create = create_cookie # 이 함수를 쿠키 클래스에 넣어서 사용함
# 만들어내는 함수가 쿠키 클래스에 들어있게 됨
# 쿠키와 관련있으니 쿠키에 넣어서 사용하면 편리할 것

cookie = Cookie.create('초코칩', 300) # create_cookie함수에 의한 cookie인스턴스 생성!

def add_weight(cookie): # 쿠키의 중량을 추가하는 메소드
    cookie.weight += 1  # 쿠키의 weight속성에 1g추가
    print('{}의 중량이 {}g 가 되었습니다.'.format(cookie.name, cookie.weight))
    #출력
def sub_weight(cookie):
    cookie.weight -= 1
    print('{}의 중량이 {}g 가 되었습니다'.format(cookie.name, cookie.weight))

Cookie.add = add_weight # 쿠키 클래스와 관련된 함수이므로 클래스에 넣는다.
Cookie.sub = sub_weight # 클래스에 속하는 인스턴스의 속성을 다음과 같은 함수로 정의하는 것!
cookie.add() #쿠키 인스턴스의 add속성을 호출
cookie.sub()
