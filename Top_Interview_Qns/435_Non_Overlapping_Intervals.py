class Solution:
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda x: x[0])

        
        intervals_to_remove = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:

            if (start >= prev_end):
                # not overlapping
                prev_end = end
            else:
                intervals_to_remove += 1
                prev_end = min(end, prev_end)


        return intervals_to_remove