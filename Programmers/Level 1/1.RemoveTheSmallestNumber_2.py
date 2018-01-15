def rm_small(mylist):
    return [x for x in mylist if not x==min(mylist)]



# mylist = [3,5,2,4]
print(rm_small([3,5,2,4]))



# def rm_small(mylist):
#     # 함수를 완성하세요
#     temp = mylist[:]
#     mylist.sort()
#     temp.remove(mylist[0])
#     mylist = temp
#     return mylist
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# my_list = [4, 3, 2, 1]
# print("결과 {} ".format(rm_small(my_list)))
