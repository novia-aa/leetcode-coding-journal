class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the set already sorted, so could use binary search directly
        tail = len(nums) -1
        front = 0

        while front <= tail :
            mid = (front + tail) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                front = mid +1
                
            elif nums[mid] > target:
                tail = mid -1
           
            
        return -1
    """
    標準寫法 while front <= tail
    """
            
