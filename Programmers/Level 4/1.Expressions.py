def expressions(num):

    answer = 0
    for i in range(1,num+1):
        result = 0
        for j in range(i, num+1):
            result += j
            if result == num:
                answer += 1
                break
            elif result > num:
                break
    return answer



print(expressions(20))


'''<Clean Code>
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
'''
