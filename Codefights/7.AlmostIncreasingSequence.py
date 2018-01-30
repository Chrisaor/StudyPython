def almostIncreasingSequence(sequence):
    j = 0
    temp = list(sequence)
    for i in range(1,len(sequence)):
        if j == 1:
            for k in range(1,len(temp)):
                print(k)
                if temp[k] <= temp[k-1]:
                    return False
            return True

        elif sequence[0] >= sequence[i]:
            temp.remove(sequence[0])
            j += 1
            print(i)
            print(temp)

        elif sequence[i] <= sequence[i-1]:
            print('idx: ',i, 'value: ', sequence[i])
            print('found' ,temp)
            if sequence[i] <= sequence[i-2]:
                del temp[i]
            else:
                del temp[i-1]
            print('removed', temp)
            j += 1

    return True

sequence = [1, 2, 3, 4, 3, 6]

print(almostIncreasingSequence(sequence))
