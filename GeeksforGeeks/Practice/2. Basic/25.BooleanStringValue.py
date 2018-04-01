def boolean_string(bool_string):
    calc = list()
    for i in bool_string:
        calc.append(i)

    while len(calc) != 1:
        if calc[0] == '0':
            X = 0
        else:
            X = 1

        if calc[2] == '0':
            Y = 0
        else:
            Y = 1

        if calc[1] == 'A':
            calc[:3] = [str(X&Y)]
        elif calc[1] == 'B':
            calc[:3] = [str(X|Y)]
        else:
            calc[:3] = [str(X^Y)]

    return str(calc[0])

t = int(input())
for i in range(t):
    bool_string = input()
    print(boolean_string(bool_string))
