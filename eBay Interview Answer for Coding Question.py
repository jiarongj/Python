def function(arr):
    output = []
    for i in range(len(arr)-1):
        if arr[i] != 0:
            k = i+1
            while arr[k] & arr[k] == 0:
                k += 1
            if arr[i] == arr[k]:
                arr[k] = 0
                arr.append(arr[i]*2)
    count = 0
    for j in range(len(arr)-1, -1, -1):
        if arr[j] == 0:
            count += 1
            del arr[j]
    for tk in range(count):
        output.append(0)
    arr = arr + output
    return arr

print(function([2,2,0,2,0,4,8,0]))

# output as [2, 2, 4, 8, 4, 0, 0, 0, 0]
# should not have used a set as input since print({2,2,0,2,0,4,8,0}) >> {0,8,2,4}.
# arr[] = {1,2,3} correspond to a list [] in python