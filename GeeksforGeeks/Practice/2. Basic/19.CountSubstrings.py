def count_substrings(str1):
    answer = 0
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if str1[i] == '1':
                if str1[j] == '1':
                    answer += 1
    return str(answer)

t = int(input())
for i in range(t):
    str1 = input()
    print(count_substrings(str1))
