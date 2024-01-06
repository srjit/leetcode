class Solution:

    def maximumCount(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1
        number_of_negative_nums = None

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < 0:
                number_of_negative_nums = mid
                left = mid + 1  # Look in the right half for a larger negative number
            else:
                right = mid - 1 


        left, right = 0, len(nums) - 1
        number_of_positive_nums = None

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > 0:
                number_of_positive_nums = mid
                right = mid - 1  # Look in the left half for a smaller positive number
            else:
                left = mid + 1

        
        count_n = number_of_negative_nums+1 if number_of_negative_nums is not None else 0
        count_p = len(nums)-number_of_positive_nums if number_of_positive_nums is not None else 0
        return max(count_n, count_p)


        