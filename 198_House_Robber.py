

class Solution:

    def rob(self, nums: List[int]) -> int:

        #[rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0 
        for n in nums:
            temp = rob1
            rob1 = max(rob(n+rob1), rob2)
            rob2 = temp

        return rob1
        