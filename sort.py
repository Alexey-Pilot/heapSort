from random import randint

nums = [randint(0, 50) for i in range(10)]
print(nums)
x = nums[5]


def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


quicksort(nums, 0, len(nums))
print('Sorted list: ', end='')
print(nums)


def binary_search(lst, num, count=0):
    pos = lst[len(lst) // 2]
    if pos == x:
        count += 1
        return (x, count)
    if pos > x:
        count += 1
        binary_search(lst[:pos], num, count)
    else:
        count += 1
        binary_search(lst[pos + 1:], num, count)


binary_search(nums, x)