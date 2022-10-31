"""id = 73516132."""


def comparator(element, pivot):
    if int(element[1]) < int(pivot[1]):
        return True
    if int(element[1]) > int(pivot[1]):
        return False
    if int(element[1]) == int(pivot[1]):
        if int(element[2]) < int(pivot[2]):
            return False
        if int(element[2]) == int(pivot[2]):
            if element[0] < pivot[0]:
                return False
            if element[0] == pivot[0]:
                return True
            if element[0] > pivot[0]:
                return True
        if int(element[2]) > int(pivot[2]):
            return True


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if not comparator(array[j], pivot):
            i += 1
            array[i], array[j], = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


def quicksort_inplace(a, low=0, high=None):
    if high is None:
        high = len(a)-1
    if low < high:
        pivot_index = partition(a, low, high)
        quicksort_inplace(a, low, pivot_index - 1)
        quicksort_inplace(a, pivot_index + 1, high)


user_num = int(input())
user = []
for i in range(user_num):
    user.append([x for x in input().split()])
quicksort_inplace(user)
i = 0
for element in user:
    print(element[0])
