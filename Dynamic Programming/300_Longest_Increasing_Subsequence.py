
from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        max_seq_lengths = [1] * len(nums) 

        for i in range(len(nums)-1,-1, -1):
            for j in range(i+1, len(nums), 1):
                if nums[i] < nums[j]:
                    max_seq_lengths[i] = max(max_seq_lengths[i], 1 + max_seq_lengths[j])

        return max(max_seq_lengths)


print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
