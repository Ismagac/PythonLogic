from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()
        result = [[0, 0]]
        heap = [(0, float('inf'))]

        for x, neg_h, R in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h != 0:
                heapq.heappush(heap, (neg_h, R))

            if result[-1][1] != -heap[0][0]:
                result.append([x, -heap[0][0]])

        return result[1:]

def test_getSkyline():
    sol = Solution()
    
    buildings1 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    expected1 = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    result1 = sol.getSkyline(buildings1)
    print("Test 1:", "PASS" if result1 == expected1 else "FAIL")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    
    buildings2 = [[1, 5, 11], [2, 7, 6], [3, 9, 13], [12, 16, 7], [14, 25, 3], [19, 22, 18], [23, 29, 13], [24, 28, 4]]
    expected2 = [[1, 11], [3, 13], [9, 0], [12, 7], [16, 0], [19, 18], [22, 3], [23, 13], [29, 0]]
    result2 = sol.getSkyline(buildings2)
    print("Test 2:", "PASS" if result2 == expected2 else "FAIL")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    
    buildings3 = [[1, 5, 10]]
    expected3 = [[1, 10], [5, 0]]
    result3 = sol.getSkyline(buildings3)
    print("Test 3:", "PASS" if result3 == expected3 else "FAIL")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    
    buildings4 = []
    expected4 = []
    result4 = sol.getSkyline(buildings4)
    print("Test 4:", "PASS" if result4 == expected4 else "FAIL")
    print(f"Expected: {expected4}")
    print(f"Got: {result4}")

if __name__ == "__main__":
    test_getSkyline()

