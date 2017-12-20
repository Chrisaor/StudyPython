def rm_small(mylist):
	temp = mylist[:]
	print("temp : ",temp)
	mylist.sort()
	print("sorted mylist : ", mylist)
	print("temp : ", temp)
	temp.remove(mylist[0])
	print("removed the smallest number :", temp)
	mylist = temp
	return mylist



my_list = [3,5,7,1]

print("결과 {}".format(rm_small(my_list)))