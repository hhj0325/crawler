oldArr = [5, 10, 1, 20, 8, 7, 100, 101, 102]


def select_sort(arr):
    # 外层循环
    for i in range(len(arr)):
        small = arr[i]
        small_index = i

        # 内层循环
        for j in range(i, len(arr) - 1):
            if small > arr[j]:
                small_index = j
                small = arr[j]
        # 交换
        if small_index != i:
            temp = arr[i]
            arr[i] = arr[small_index]
            arr[small_index] = temp
        else:
            break
        print(i)
        print(arr)
    return arr


def count(i):
    print(i)
    if i <= 1:
        return
    else:
        count(i - 1)


def fact(x, y):
    if x == 1:
        return y
    else:
        return fact(x - 1, x * y)


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


def count_list(list):
    if list == []:
        return 0
    return 1 + count_list(list[1:])


def quicksort(array):
    if len(array) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # recursive case
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


select_sort(oldArr)
count(10)
print(fact(10, 1))
print(sum([1, 2, 3, 4]))
print(count_list([1, 2, 3, 4]))
