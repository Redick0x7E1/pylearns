def rotation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    key = arr1[0]
    key_index = 0

    # if I find the same as arr[0] IN arr2. Get its index value.
    for i in range(len(arr2)):
        if arr2[i] == key:
            key_index = i

            break

    if key_index == 0: # edge check if item not in arr2
        return False

    for x in range(len(arr1)):
        arr2index = (key_index + x) % len(arr1)

        if arr1[x] != arr2[arr2index]:
            return False
    return True


a = [1,2,3,4]
b = [2,3,4,1]
print(rotation(a,b))