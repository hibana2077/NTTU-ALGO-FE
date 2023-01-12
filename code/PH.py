
def binary_search_with_counter(array, target):
    """
    Returns the index of the target in the array if it exists, otherwise returns -1.
    """
    counter = 0
    left = 0
    right = len(array) - 1
    while left <= right:
        counter += 1
        mid = (left + right) // 2
        if array[mid] == target:
            return counter
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return counter

while True:
    try:
        arr = list(map(int, input().split()))
        target = int(input())
        print(binary_search_with_counter(arr, target)) if target in arr else print(-1)
    except EOFError:break