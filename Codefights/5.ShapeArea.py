def shapeArea(n):
    answer = 1
    if n == 1:
        return 1
    else:
        for i in range(1,n):
            answer += 4*i
    return answer


print(shapeArea(4))
