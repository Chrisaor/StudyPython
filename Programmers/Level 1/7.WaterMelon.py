def water_melon(n):
	str = ''
	for i in range(n):
		if i % 2 == 0:
			str += '수'
		else:
			str += '박'
	return str


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

'''<Clean Code>
def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
'''