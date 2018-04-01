def allLongestStrings(inputArray):
    result = list()
    max_str_len = 0
    for i in inputArray:
        if max_str_len < len(i):
            max_str_len = len(i)

    for j in inputArray:
        if len(j) == max_str_len:
            result.append(j)

    return result



inputArray = ["aba", "aa", "ad", "vcd", "aba"]

print(allLongestStrings(inputArray))
