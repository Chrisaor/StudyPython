def toWeirdCase(s):
    answer = []
    list1 =s.lower().split(" ")
    for i in range(len(list1)):
        str1 = ''
        for j in range(len(list1[i])):
            if j % 2 ==0:
                str1 += list1[i][j].upper()
            else:
                str1 += list1[i][j]
        answer.append(str1)
    return " ".join(answer)


print("결과 : {}".format(toWeirdCase("try hello world")));

'''<Clean Code>
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
'''
