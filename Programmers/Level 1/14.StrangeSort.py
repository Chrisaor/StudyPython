def strange_sort(strings, n):
    temp = []
    result = []
    for i in range(len(strings)):
        temp.append(strings[i][n:]+str(i))
        temp.sort()
    for j in range(len(strings)):
        result.append(strings[int(temp[j][-1])])
    return result

print( strange_sort(["sun", "bed", "car"], 1) )

'''<Clean Code>
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))
'''
