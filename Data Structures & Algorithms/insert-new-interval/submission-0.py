class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ret = [intervals[0]]
        for i in range(len(intervals)):
            prev_start, prev_end = ret.pop()
            curr_start, curr_end = intervals[i]

            if curr_start <= prev_end: # overlap
                ret.append((min(prev_start, curr_start), max(prev_end, curr_end)))
            else: 
                ret.append((prev_start, prev_end))
                ret.append((curr_start, curr_end))

        return ret