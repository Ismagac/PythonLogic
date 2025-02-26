from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        max_product = nums[0]  
        min_product = nums[0]  
        max_so_far = nums[0] 

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product 

            max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
            min_product = min(nums[i], max_product * nums[i], min_product * nums[i])

            max_so_far = max(max_so_far, max_product)

        return max_so_far 