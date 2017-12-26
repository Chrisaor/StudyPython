def string_middle(str):
    if len(str) % 2 == 0:
        return str[len(str)//2 - 1] + str[len(str)//2]
    else:
        return str[len(str)//2]


print(string_middle("power"))

'''<Clean Code>
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
'''
