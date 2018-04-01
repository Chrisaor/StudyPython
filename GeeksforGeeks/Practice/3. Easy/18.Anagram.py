def anagram(str1, str2):
    str1 = sorted(list(str1))
    str2 = sorted(list(str2))
    if str1 == str2:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    print(anagram(str1,str2))
