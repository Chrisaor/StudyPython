def reverseStr(str1):
    strList = str1.split(".")[::-1]
    answer = '.'.join(strList)
    return answer

t = int(input())
for i in range(t):
    str1 = input()
    print(reverseStr(str1))

    
