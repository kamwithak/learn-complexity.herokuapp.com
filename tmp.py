def fastRecursive(low, high, arr, target):
    if low > high:
        return False

    mid = (high + low)//2
    if target == arr[mid]:
        return True

    if target < arr[mid]:
        return fastRecursive(low, mid-1, arr, target)
    else:
        return fastRecursive(mid+1, high, arr, target)

arr = [1,2,3,4,5,6,7,8,9]
#print(slowSearch(arr, 34))
#print(fastIterative(arr, 34))
print(fastRecursive(0,len(arr)-1,arr,91))