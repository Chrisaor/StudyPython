def arrayChange(inputArray):
    sum1 = 0
    for i in range(len(inputArray)):
        temp = list()
        if i == 0:
            continue
        else:
            if inputArray[i] > inputArray[i-1]:
                continue
            else:
                temp.append(inputArray[i])
                inputArray[i] = inputArray[i-1] +1
                sum1 += inputArray[i] - temp[0]
    return sum1

arr = [1,1,1]
print(arrayChange(arr))
