
from typing import List

def search(arr: List, target: int) -> int :

    low = 0
    high = len(arr)-1

    mid_prev = -9999

    while low <= high:

        mid = (low+high)//2
        
        
        if arr[mid] < target:
            low = mid+1
        elif arr[mid] > target:
            high = mid
        else:
            return mid
        
        mid_prev = mid

    
    return -1

print(search([5,7,7,8,8,10], 8))
