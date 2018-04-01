def bitnoic_subarr(arr):
    asc = 0
    des = 0
    temp = list()
    result = list()

    if len(arr) == 1:
        return 1
    elif len(arr) == 2:
        return 2
        
    for i in range(len(arr)):
        if len(temp) == 0:
            temp.append(arr[i])

        elif asc == 0 and des == 0:
            temp.append(arr[i])
            if temp[-1] < temp[-2]:
                des = 1
            elif temp[-1] > temp[-2]:
                asc = 1
            else:
                asc = 0
                des = 0

        elif asc == 1 and des == 0: # asc모드
            if temp[-1] > arr[i]:  # 낮은 원소 발견
                asc = 0 # asc모드 종료
                des = 1 # des모드 시작
                temp.append(arr[i]) # temp에 넣고
                if i == len(arr)-1:  # 마지막 원소이면
                    result.append(len(temp)) # temp길이를 result에 삽입
                    if len(result) == 0:
                        return 0
                    elif len(result) == 1:
                        return result[0]
                    else:
                        return max(result)
            elif temp[-1] < arr[i]:
                temp.append(arr[i])
                if i == len(arr)-1:  # 마지막 원소이면
                    result.append(len(temp)) # temp길이를 result에 삽입
                    if len(result) == 0:
                        return 0
                    elif len(result) == 1:
                        return result[0]
                    else:
                        return max(result)
            else:
                temp.append(arr[i])
                temp = temp[-1:]
                asc = 0
                des = 0

        elif asc == 0 and des == 1:
            if temp[-1] < arr[i]:
                result.append(len(temp))
                asc = 0
                des = 0
                temp = temp[-1:]

            if temp[-1] > arr[i]:
                temp.append(arr[i])
                if i == len(arr)-1:
                    result.append(len(temp))
                    if len(result) == 0:
                        return 0
                    elif len(result) == 1:
                        return result[0]
                    else:
                        return max(result)
            elif temp[-1] < arr[i]:
                temp.append(arr[i])
                if i == len(arr)-1:
                    result.append(len(temp))
                    if len(result) == 0:
                        return 0
                    elif len(result) == 1:
                        return result[0]
                    else:
                        return max(result)
            else:
                temp.append(arr[i])
                temp = temp[-1:]
                asc = 0
                des = 0

    if len(result) == 0:
        return 0
    else:
        return max(result)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(bitnoic_subarr(arr))

arr_str = '521 791 925 189 764 941 852 663 830 901 714 959 579 366 8 478 201 59 440 304 761 358 325 478 109 114 888 802 851 461 429 994 385 406 541 112 705 836 357 73 351 824 486 557 217 627 358 527 358 338 272 870 362 897 23 618 113 718 697 586 42 424 130 230 566 560 933 297 856 54 963 585 735 655 973 458 370 533 964 608 484 912 636 68 849 676 939 224 143 755 512 742 176 460 826 222 871 627 935 206 784 851 399 280 702 194 735 638 535 557 994 177 706 963 549 882 301 414 642 856 856 143 463 612 878 425 679 753 444 297 674 41 314 876 73 819 611 18 933 113 696 170 832 41 489 686 91 498 590 991 146 354 315 652'
arr = arr_str.split(' ')
print(bitnoic_subarr(arr))
