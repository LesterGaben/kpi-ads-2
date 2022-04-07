from random import shuffle

def comb_sort(array):
    swapped = False
    n = len(array)
    gap = int(n/1.247)
    count_of_comparisons = 0
    count_of_swaps = 0
    while gap > 1 or swapped == True:
        swapped = False
        for i in range(n - gap):
            count_of_comparisons += 1
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                count_of_swaps += 1
                swapped = True
        if gap > 1:
            gap = int(gap/1.247)
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
    comb_sort(array)
    pass


