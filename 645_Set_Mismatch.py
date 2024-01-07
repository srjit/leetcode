from collections import Counter

class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:

        _limit = len(nums)
        _sum = (_limit * (_limit+1))//2

        missing_number = _sum - sum(set(nums))
        duplicate_number = sum(nums) + missing_number - _sum
        return [duplicate_number, missing_number]


        

            
        