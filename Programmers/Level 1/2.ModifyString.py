def alpha_string46(s):
	print(len(s))
	if len(s) == 4 or len(s) == 6:
		for i in s:
			if i in ['1','2','3','4','5','6','7','8','9','0']:
				continue
			else:
				return False
		return True
	else:
		return False


print( alpha_string46("a234") )
print( alpha_string46("2825") )

'''<Clean Code>
def alpha_string46(s):
    return s.isdigit() and len(s) in [4, 6]

print( alpha_string46("a234") )
print( alpha_string46("1234") )'''
