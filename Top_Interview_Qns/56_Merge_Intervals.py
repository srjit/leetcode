from typing import List
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])

        output = [intervals[0]]
        for interval in intervals:
            prev = output[-1]
            if prev[1] >= interval[0]:
                output[-1][1] = max(prev[1], interval[1])
            else:
                output.append(interval)

        return output


print(Solution().merge([[1,4],[4,5]]))
                


