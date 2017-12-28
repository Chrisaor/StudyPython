def adder(a, b):
    result = 0
    if a == b:
        return a
    else:
        for i in range(min(a,b), max(a,b)+1):
            result += i
        return result

print(adder(3, 5))


'''<Clean Code>
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))

print( adder(3, 5))
'''
