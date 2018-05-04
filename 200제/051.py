class MyClass:
    def sayHello(self):
        print('안녕하세요')

    def sayBye(self, name):
        print(f'{name}! 다음에 보자!')

obj = MyClass()
obj.sayHello()
obj.sayBye('철수')
