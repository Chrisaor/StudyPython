def bin_to_decimal(bin_str):
    bin_str = bin_str[::-1]
    answer = 0
    for index, i in enumerate(bin_str):
        answer += int(i) * (2**index)
    return answer

t = int(input())
for i in range(t):
    bin_str = input()
    print(bin_to_decimal(bin_str))
