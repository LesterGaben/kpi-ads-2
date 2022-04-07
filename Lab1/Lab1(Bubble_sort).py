from random import shuffle

def bubble_sort(array):
    n = len(array)
    count_of_comparisons = 0
    count_of_swaps = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            count_of_comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                count_of_swaps += 1
    print("\narray size:",n)
    print("Count of comparisons: " + str(count_of_comparisons))
    print("Count of swaps: " + str(count_of_swaps))
    

for i in range(7):
    if i == 0: n = 10
    elif i == 1: n = 100
    elif i == 2: n = 1000
    elif i == 3: n = 5000
    elif i == 4: n = 10000
    elif i == 5: n = 20000
    else: n = 50000
    array = list(range(1, n + 1))
    shuffle(array)
    bubble_sort(array)
    pass



