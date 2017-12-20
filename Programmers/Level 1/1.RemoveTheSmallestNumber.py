def rm_small(mylist):
	temp = mylist[:]
	mylist.sort()
	temp.remove(mylist[0])
	mylist = temp
	return mylist



my_list = [3,5,7,1]

print("결과 {}".format(rm_small(my_list)))

'''<Clean Code>
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))'''