class Solution:
    def findMin(self, nums: List[int]) -> int:
        # set left, right, 
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # 最小值在右邊
                left = mid + 1
            else:
                # 最小值在左邊（包含 mid）
                right = mid
                
        return nums[left]








        """
        two elements for using binary search
        1. assorted array
        2. find the min ....
        """
        
