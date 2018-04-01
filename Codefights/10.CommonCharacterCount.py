def commonCharacterCount(s1, s2):
    s1_list = list()
    s2_list = list()

    for i in s1:
        s1_list.append(i)

    for i in s2:
        s2_list.append(i)

    cnt = 0
    for i in s1_list:
        if i in s2_list:
            s2_list.remove(i)
            cnt += 1
    return cnt
