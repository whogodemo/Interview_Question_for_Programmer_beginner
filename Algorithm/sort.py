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

#퀵정렬
def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right >= start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        else:
            array[left], array[right] = array[right], array[left]


    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


#quick_sort(array, 0, len(array)-1)
