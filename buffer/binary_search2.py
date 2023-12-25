from typing import List

def search(arr: List) -> int :

    low = 0
    high = len(arr)-1

    while low < high:

        mid = (low+high)//2
        
        if arr[high] < arr[mid]:
            # lowest element is in the second half
            low = mid+1
        else:
            high=mid

    return arr[low]

print(search([8,8,10, 5,7,7]))
