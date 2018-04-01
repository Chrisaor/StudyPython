class Human(): # 인간에 대한 클래스 생성
    '''인간'''

person = Human() #인스턴스 생성
person.name = '철수' #인스턴스의 name속성은 철수
person.weight = 60.5 #인스턴스의 weight속성은 60.5

def create_human(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

Human.create = create_human

person = Human.create('철수', 60.3)

def eat(person):
    person.weight += 0.1
    print("{} 가 먹어서 {} kg이 되었습니다".format(person.name, person.weight))

def walk(person):
    person.weight -= 0.1
    print('{} 가 먹어서 {} kg이 되었습니다.'.format(person.name, person.weight))

Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()
