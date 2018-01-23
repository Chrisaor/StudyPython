def subarraySum(sum_result, arr):
    answer = []
    result = ""
    for i in range(len(arr)):
        temp = []
        for j in range(i,len(arr)):
            temp.append(arr[j])
            if sum(temp) == sum_result:
                answer.append(str(i+1))
                answer.append(str(j+1))
                result = " ".join(answer)
                return result
            elif sum(temp) > sum_result:
                break;
    return -1

t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    sum_result = n[1]
    arr = list(map(int, input().split()))
    print(subarraySum(sum_result, arr))
