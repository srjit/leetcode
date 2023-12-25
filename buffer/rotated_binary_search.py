
def rotated_binary_search(arr, target):

    left, right = 0, len(arr)

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == target:
                return mid

        # if first part is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid+1
            else:
                right = mid-1 
    return -1

print(rotated_binary_search([2,5,8,9,13,15], 15))
