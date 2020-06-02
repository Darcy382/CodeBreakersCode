
# O(nlogn) runtime, O(1) space
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    i = 0
    while i < len(intervals) - 1:
        while i < len(intervals) - 1 and intervals[i][1] >= intervals[i + 1][0]:
            # Merge the intervals
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            intervals.pop(i + 1)
        i += 1
    return intervals

# Nexttime try using a new list for the intervals, and us a for loop and if statement