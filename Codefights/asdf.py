def lineEncoding(s):

    temp = list()
    result = list()
    for i in range(len(s)):
        if i == 0:
            temp.append(s[i])
        elif s[i] == s[i-1]:
            temp.append(s[i])
        elif s[i] != s[i-1]:
            if len(temp) > 1:
                result.append(str(len(temp))+temp[0])
            else:
                result.append(temp[0])
            temp = []
            temp.append(s[i])
        if i == len(s)-1:
            if len(temp) > 1:
                result.append(str(len(temp))+temp[0])
            else:
                result.append(temp[0])

    return ''.join(result)


s = "aabbbccc"
print(lineEncoding(s))
