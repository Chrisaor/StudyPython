def fibonacci(num):
	list1 = [0, 1]
	if num == 1:
		print(1)
	else:	
		for i in range(2, num+1):
			list1.append(list1[i-1]+list1[i-2])	
			print(list1, num)
		return list1[num]


print(fibonacci(4))


'''<Clean Code>
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))'''