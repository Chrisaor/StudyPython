def sort_dictionary(dic):
    tup1 = tuple(dic.items())
    list1 = []
    for i in range(len(tup1)):
        list1.append(tup1[i])
        list1.sort()

    return list1




print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))

'''<Clean Code>
def sort_dictionary(dic):
    return sorted(dic.items())
print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))
'''
