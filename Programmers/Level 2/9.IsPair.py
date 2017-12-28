def is_pair(s):
    list1 = []
    for i in range(len(s)):
        if s[i] == "(":
            list1.append(s[i])
        elif s[i] == ")":
            try:
                list1.pop()
            except IndexError:
                return False
    return list1 == []


print( is_pair("(hello)()"))
print( is_pair(")("))
