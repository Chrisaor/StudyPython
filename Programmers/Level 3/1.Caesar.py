def caesar(s, n):
    listUpper = ["A", "B", "C", "D", "E", "F", "G",
     "H", "I", "J", "K", "L", "M", "N", "O",
     "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    listLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"
    , "w", "x", "y", "z"]
    encodedStr = ""
    encodedStr = ""
    for i in s:
        if i == " ":
            encodedStr += i
        elif i == i.upper():
            print(listUpper.index(i) + n)
            encodedStr += listUpper[(listUpper.index(i)+n)%26]

        elif i != i.upper():
            print(listLower.index(i) + n)
            encodedStr += listLower[(listLower.index(i)+n)%26]

    return encodedStr

print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))

'''<Clean Code>
def convert(c, n):
    converted = ord(c) + n%26
    if (c.islower() and not chr(converted).islower()) or (c.isupper() and not chr(converted).isupper()):
        converted -= 26
    return chr(converted)

def caesar(s, n):
    return ''.join(convert(c, n) if c.isalpha() else c for c in s)

# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
'''
