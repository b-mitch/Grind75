'''Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).'''

# Simple one liner that sorts based on Euclidian distance and returns the first k items
# def k_closest(points, k):
#     return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]

# Using a heap - slower than above solution but should be faster...idk
import heapq

# Helper function to define process points
def process(point):
    return point[0] ** 2 + point[1] ** 2

def k_closest(points, k):
    # Create a list of tuples with the euclidian distance as the first value for heap operations
    processed_points = [(process(point), point) for point in points]
    # This pushes each point onto the heap and runs bubble up
    heapq.heapify(processed_points)
    output = []
    # Pop k items from the heap and append to output
    for _ in range(k):
        output.append(heapq.heappop(processed_points)[1])
    return output





# TESTS

print(k_closest([[1,3],[-2,2]], 1))
# >>[[-2,2]]

print(k_closest([[3,3],[5,-1],[-2,4]], 2))
# >>[[3,3],[-2,4]]
