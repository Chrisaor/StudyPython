# 3.1
year_list = list()
for i in range(1980, 1980+5):
    year_list.append(i)

print(year_list)

# list comprehension으로 풀기

# year_list2 = [i for i in range(1980, 1980+5)]
# print(year_list2)


# 3.2
print(year_list[3])

# 3.3
print(year_list[-1])

# 3.4
things = ['mozzarella', 'cinderella', 'salmonella']

# 3.5

things[1] = things[1].capitalize()
print(things)

# 3.6

things[0] = things[0].upper()
print(things)

# 3.7

del things[2]
print(things)

# 3.8

surprise = ['Groucho', 'Chico', 'Harpo']

# 3.9

surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print(surprise)

# 3.10

f2e = {
'dog' : 'chien',
'cat' : 'chat',
'walrus':'morse'
}

print(f2e)

# 3.11

print(f2e['walrus'])

# 3.12

e2f = dict()
for e, f in f2e.items():
    e2f[f]=e

print(e2f)

# 3.13

print(f2e['cat'])

# 3.14

print(e2f.keys())

# 3.15

life = {
'animals' : {'cats' : 'Henri'},
'plants' : {'octopi': 'Grumpy'},
'others' : {'emus':'Lucy'},
}

# 3.16

print(life.keys())

# 3.17

print(life['animals'].keys())

# 3.18

print(life['animals']['cats'])
