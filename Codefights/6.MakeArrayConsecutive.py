def makeArrayConsecutive2(statues):
    arr = sorted(status)
    i = arr[0]
    j = 1
    result = list()
    while i != arr[-1]:
        i += 1
        if i not in arr:
            result.append(i)
        else:
            continue
    return len(result)




status = [6, 2, 3, 8]
print(makeArrayConsecutive2(status))
