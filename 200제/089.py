numstr = input('숫자를 입력하세요:')
try:
	num = int(numstr)
	print(f'당신이 입력한 숫자는 정수 {num}입니다.')
except:
	try:
		num = float(numstr)
		print(f'당신이 입력한 숫자는 실수 {num}입니다.')
	except:
		print('+++ 숫자를 입력하세요~ +++')
