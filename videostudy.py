def bubble_sort(arr):

    """
    Use bubble_sort algorithim to sort a list of numbers.
    Input: List of integers (will work for strings as well)
    Output: Sorted list of integers

    """

    swap_happened = True
    while swap_happened:
        print('Bubble sort status ' + str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

l = [6,8,1,4,10,7,12,6,8,6,2]

print(bubble_sort(l))

