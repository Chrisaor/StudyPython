def average(list):
	sum = 0
	for i in range(len(list)):
		sum += list[i]	
	return (sum / len(list))


list = [5,3,4]
print("평균값 : {}".format(average(list)))


'''<Clean Code>
def average(list):
    return (sum(list) / len(list))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
