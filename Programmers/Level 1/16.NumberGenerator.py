def number_generator(x, n):
    result = []
    num = 0
    for i in range(n):
        num += x
        result.append(num)
    return result

print(number_generator(3,5))


'''<Clean Code>
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
'''
