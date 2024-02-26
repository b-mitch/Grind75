'''You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.'''

def interval_overlaps(interval, new_interval):
    # Does not overlap if its before or after the current interval
    if interval[0] > new_interval[1] or interval[1] < new_interval[0]:
        return False
    return True

def merge_intervals(intervals, start, end, new_interval):
    merged_intervals = [None, None]
    # Start of merged interval is the smaller of new interval start and first overlapping interval start
    merged_intervals[0] = new_interval[0] if new_interval[0] < intervals[start][0] else intervals[start][0]
    # End of merged interval is the larger of the new interval end and the last overlapping interval end
    merged_intervals[1] = new_interval[1] if new_interval[1] > intervals[end][1]  else intervals[end][1]
    # Return all intervals including the merged interval
    return intervals[:start] + [merged_intervals] + intervals[end + 1:]

def insert_interval(intervals, new_interval):
    # Account for empty intervals input
    if not intervals:
        return [new_interval]
    start = end = None
    # Iterate intervals checking for overlaps with new interval
    for i, interval in enumerate(intervals):
        # Be sure to check if the interval fits without overlapping
        if i < len(intervals) - 1 and new_interval[0] > interval[1] and new_interval[1] < intervals[i + 1][0]:
            return intervals[:i + 1] + [new_interval] + intervals[i + 1:]
        # If there is an overlap, save the index as either the start of end of the overlap
        if interval_overlaps(interval, new_interval):
            if start is None:
                start = i
            else:
                end = i
    # If there have been no overlaps then the new_interval either comes before or after intervals
    if start is None:
        return intervals + [new_interval] if intervals[-1][1] < new_interval[0] else [new_interval] + intervals
    # If there is only one overlapping interval set end and start equal
    if end is None:
        end = start
    return merge_intervals(intervals, start, end, new_interval)



# TESTS

print(insert_interval([[1,3],[6,9]], [2,5]))
# >> [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# >> [[1,2],[3,10],[12,16]]
print(insert_interval([[3,5],[12,15]], [6,6]))
# >> [[1,11]]