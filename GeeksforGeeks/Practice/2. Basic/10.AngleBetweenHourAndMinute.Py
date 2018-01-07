def angleOfClock(h, m):

    MinuteAngle = (m * 6) % 360
    HourAngle = h*30 + (((m % 60)/60) * 30)
    bwAngle = abs(MinuteAngle - HourAngle)
    if bwAngle > 180:
        return abs(int(bwAngle - 360))
    else:
        return int(bwAngle)


t = int(input())
for i in range(t):
    n = list(map(float, input().split()))
    print(angleOfClock(n[0], n[1]))
