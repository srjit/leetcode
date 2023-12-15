class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
        

s = Solution()
s.removeElement(nums=[3,2,2,3], val = 3)