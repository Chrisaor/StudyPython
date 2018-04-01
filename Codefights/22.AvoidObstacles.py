def avoidObstacles(inputArray):
    inputArray = sorted(inputArray)
    for i in range(1, 41):
        jump = 0
        print(jump)
        for j in range(inputArray[-1]+2):
            jump += i
            print(jump)
            if jump in inputArray:
                print('stepped number')
                break
            elif jump > inputArray[-1] and j == inputArray[-1]+1:
                return i


inputArray = [1,2,4,6,10]
print(avoidObstacles(inputArray))

# V@@3V567V9
# V@23V
# V12@4@6@V@@10@V
