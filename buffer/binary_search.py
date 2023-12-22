
from typing import List

def search(arr: List, elt: int) -> int :

    low = 0
    high = len(arr)

    while low <= high:

        mid = (low+high)//2
        if arr[mid] == elt:
            return mid
        elif arr[mid] < elt:
            high = mid-1
        else:
            low = mid+1

    return -1

print(search([2,5,8,9,13,15], 9))
