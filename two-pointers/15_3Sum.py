class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums.sort()
        # set ans as set
        ans =set()
        # start from index 0 to len(nums)-2
        for i in range(0, len(nums)-2):
            target = -(nums[i])
            # set the front and tail pointer
            front=i+1
            tail =len(nums)-1
            # find anns the others in the list 
            while front < tail:
                if nums[front] + nums[tail] == target:
                    ans.add(tuple([nums[i], nums[front], nums[tail]]))
                    front+=1
                    tail-=1
                    
                if nums[front] + nums[tail] > target:
                    tail-= 1

                if nums[front] + nums[tail] < target:
                    front+= 1
            
        
        return list(ans)

        # hint 用 set(ans) 嘗試去重，但 ans 是 list of lists，不能直接去重
