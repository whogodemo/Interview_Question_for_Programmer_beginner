a = [9, 1, 3, 4, 6, 2, 0, 10]

#선택정렬
for i in range(len(a)):
    index = i
    for j in range(i, len(a)):
        if a[j] < a[index]:
            index = j

    a[index], a[i] = a[i], a[index]

#버블정렬
for i in range(len(a), 1, -1):
    for j in range(1, i):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
