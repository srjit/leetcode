from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_pro = [1]
        suffix_pro = [1]
        pro = 1
        for i in range(1, len(nums)):
            pro *= nums[i-1]
            prefix_pro.append(pro)
        pro = 1
        for i in range(len(nums)-2,-1,-1):
            pro *= nums[i+1]
            suffix_pro.append(pro)

        import ipdb
        ipdb.set_trace()

        op = []
        for i in range(len(nums)):
            res = prefix_pro[i] * suffix_pro[len(nums)-i-1]
            op.append(res)
            
        return op







print(Solution().productExceptSelf([1,2,3,4]))

        