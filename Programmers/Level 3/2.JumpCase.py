from math import factorial
def jumpCase(num):

    list1 = []
    route = 0
    for i in range(0,num+1):
        for j in range(0,num+1):
            result = i + 2 * j
            if result == num:
                list1.append([i, j])
                result = 0
    for k in range(len(list1)):
        if 0 in list1[k]:
            route += 1
        else:
            factorialresult = factorial(list1[k][0] + list1[k][1])/(factorial(list1[k][0])*factorial(list1[k][1]))
            route += int(factorialresult)
    return route

print(jumpCase(4))

'''<Clean Code>
def jumpCase(num):
    answer = 0
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return jumpCase(num-1)+jumpCase(num-2)

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))
'''
