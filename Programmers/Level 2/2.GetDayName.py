def getDayName(a,b):

    accDay = {
    1:0,
    2:31,
    3:60,
    4:91,
    5:121,
    6:152,
    7:182,
    8:213,
    9:245,
    10:275,
    11:305,
    12:335,
    }
    dayStr = {
    1:"FRI",
    2:"SAT",
    3:"SUN",
    4:"MON",
    5:"TUE",
    6:"WED",
    0:"THU",
    }
    numDay = accDay[a]+b
    c = numDay % 7
    answer = dayStr[c]
    return answer


print(getDayName(1,30))

'''<Clean Code>
from datetime import *

def getDayName(a,b):
    s = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return s[datetime(year = 2016, month = a, day = b).weekday()]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
'''
