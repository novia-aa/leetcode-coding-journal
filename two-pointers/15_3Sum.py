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
                    
                elif nums[front] + nums[tail] > target:
                    tail-= 1

                elif nums[front] + nums[tail] < target:
                    front+= 1
            
        
        return list(ans)

        # hint 用 set(ans) 嘗試去重，但 ans 是 list of lists，不能直接去重

###################################################################################
# considering remove the dupicated elememnt
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums.sort()
        # set ans as set
        ans =[]
        # start from index 0 to len(nums)-2
        for i in range(0, len(nums)-2):
            # avoid duplicated
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            target = -(nums[i])
            # set the front and tail pointer
            front=i+1
            tail =len(nums)-1
            # find anns the others in the list 
            while front < tail:
                
                if nums[front] + nums[tail] == target:
                    ans.append([nums[i], nums[front], nums[tail]])
                     # Skip duplicate front
                    while front < tail and nums[front] == nums[front + 1]:
                        front += 1
                    # Skip duplicate tail
                    while front < tail and nums[tail] == nums[tail - 1]:
                        tail -= 1
                    front+=1
                    tail-=1
                    
                elif nums[front] + nums[tail] > target:
                    tail-= 1

                elif nums[front] + nums[tail] < target:
                    front+= 1
            
        
        return ans

# hint 用 set(ans) 嘗試去重，但 ans 是 list of lists，不能直接去重
