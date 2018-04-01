def remaining_string(str1, key, num):
    str_list = list(str1)
    if num == 0:
        return str1

    try:
        for i in range(num-1):
            str_list.remove(key)
    except ValueError:
        return 'Empty string'

    if key in str_list:
        if str_list.index(key) == len(str_list)-1:
            return 'Empty string'
        else:
            return ''.join(str_list[str_list.index(key)+1:])
    else:
        return 'Empty string'

t = int(input())
for i in range(t):
    str1 = str(input())
    key = str(input())
    num = int(input())
    print(remaining_string(str1, key, num))
