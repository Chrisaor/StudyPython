def islucky(n):
    m = str(n)
    count_front = 0
    count_rear = 0
    for i in range(len(m)//2):
        count_front += int(m[i])

    for i in range(len(m)//2, len(m)):
        count_rear += int(m[i])

    return True if count_front==count_rear else False


n = '123050'

print(is_lucky(n))
