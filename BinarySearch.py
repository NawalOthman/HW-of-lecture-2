def binarySearch(numbers, n, first, last):
    while first <= last:
        mid = first + (last - first)//2
        if numbers[mid] == n:
            return mid
        elif numbers[mid] < n:
            first = mid + 1
        else:
            last = mid - 1
    return "Not Found"

numbers = [3, 4, 5, 6, 7, 8, 9]
n = 6
result = binarySearch(numbers, n, 0, len(numbers)-1)

if result != "Not Found":
    print("Element is present at index " + str(result))
else:
    print("Not Found")