class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_target = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == new_target:
                    return [i,j]


"""
the question ask for the polarized value again, but it doesn't mention the array is sorted or not
So  I would not use binary search to solve the issue
"""
        
