def rotate(arr, d):
    n = len(arr)
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i = i + 1
    i = 0
    while d < n:
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[:i] + temp
    return arr


arr = [1, 2, 3, 5, 4, 6]
d = 3
print("Original array:", arr)
rotated_array = rotate(arr, d)
print("Rotated array:", rotated_array)
