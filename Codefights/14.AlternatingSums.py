def alternatingSums(a):
    team1 = list()
    team2 = list()
    for i in range(len(a)):
        if i % 2 == 0:
            team1.append(a[i])
        else:
            team2.append(a[i])
    return [sum(team1), sum(team2)]

a = [50, 50, 60, 40, 70]
print(alternatingSums(a))
