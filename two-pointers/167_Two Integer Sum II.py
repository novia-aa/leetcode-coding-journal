class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers
        front =0
        tail = len(numbers)-1
        
        while front < tail:
            # if cur sum == target
            if (numbers[front]+ numbers[tail]) == target:
                # return index
                return [front+1, tail+1]
            # if cur sum < target
            if (numbers[front]+ numbers[tail]) < target:
                front +=1
            # if cur sum > target
            if (numbers[front]+ numbers[tail]) > target:
                tail -=1
