from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Group numbers into numbers that are > 0,  = 0 and < 0

        nums = sorted(nums)

        group_N = list(filter(lambda x: x < 0, nums))
        group_P = list(filter(lambda x: x > 0, nums))
        group_Z = list(filter(lambda x: x == 0, nums))

        group_n_d = {x: "" for x in group_N}
        group_p_d = {x: "" for x in group_P}

        combinations = []
        if len(group_Z) > 0:
            if len(group_Z) >= 3:
                combinations += [(0,0,0)]

            for p_elt in group_P:
                # check if group_P's complement is present in group_N
                if  -p_elt in group_n_d and (p_elt, 0, -p_elt) not in combinations:
                    combinations.append((p_elt, 0, -p_elt))

        limit_P = len(group_P)
        for i in range(limit_P):
            for j in range(limit_P):
                if i < j:
                    sum = group_P[i] + group_P[j]
                    if -sum in group_n_d and (-sum, group_P[i], group_P[j]) not in combinations:
                        combinations.append((-sum, group_P[i], group_P[j]))

        
        limit_N = len(group_N)
        for i in range(limit_N):
            for j in range(limit_N):
                if i < j:
                    sum = group_N[i] + group_N[j]
                    if abs(sum) in group_p_d and (group_N[i], group_N[j], abs(sum)) not in combinations:
                        combinations.append((group_N[i], group_N[j], abs(sum)))

        return combinations



s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))


        