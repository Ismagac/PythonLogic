from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += max(0, right_max - height[right])
        
        return water_trapped

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  #6
print(solution.trap([4,2,0,3,2,5]))  #9