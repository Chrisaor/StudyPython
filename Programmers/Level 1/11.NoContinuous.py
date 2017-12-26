def no_continuous(s):
    strlist = []
    for i in range(len(s)):
        if s[i] not in strlist:
            if i == 0 or s[i] != s[i-1]:
                strlist.append(s[i])

    return strlist

print( no_continuous( "133303" ))

'''<Clean Code>
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print( no_continuous( "133303" ))
'''
