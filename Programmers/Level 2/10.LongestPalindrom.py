def longest_palindrom(s):
    chkS = ""
    pldlist = []
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j]:
                chkS = s[i:j+1]
                if chkS == chkS[::-1]:
                    pldlist.append(chkS)
    return len(max(pldlist, key = len))


print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))



'''<Clean Code>
def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))

print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))
'''
