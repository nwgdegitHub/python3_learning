import random
teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]

for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)
print(offices)