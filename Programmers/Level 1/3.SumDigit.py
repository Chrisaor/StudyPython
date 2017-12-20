def sum_digit(number):
	SumDigit = 0
	while number != 0:
		SumDigit += number%10
		number //= 10
	return SumDigit

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));

'''<Clean code>
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));'''

