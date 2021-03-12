list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

list2 = []
for i in range(10):
    list2.append(i)
print(list2)

list3 = [i for i in range(10)]
print(list3)

list4 = [i for i in range(10) if i % 2 == 0]
print(list4)

list5 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list5)  # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
