def removeSpace(s):
    result = []
    answer = ''
    parsedStr = s.split(' ')
    for i in range(len(parsedStr)):
        if parsedStr[i] != ' ':
            result.append(parsedStr[i])
    answer = ''.join(result)
    return answer

t = int(input())
for i in range(t):
    s = input()
    print(removeSpace(s))
