def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))

'''<Clean Code>
def evenOrOdd(num):
    return num % 2 and "Odd" or "Even"

print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
'''
