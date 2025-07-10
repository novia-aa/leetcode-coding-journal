class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # according to the instruction two bars --> use two pointers
        front, tail = 0, len(heights)-1
        max_volume = float('-inf')
        height = 0
        while front < tail:
            # if the height is smaller then the previous one continue
            while height > min(heights[front], heights[tail]):        
                if heights[front] > heights[tail] :
                    tail -= 1
                else :
                    front += 1
            else:
                height = min(heights[front], heights[tail])
                # lower height pointer move forward
                if heights[front] > heights[tail] :
                    tail -= 1
                else :
                    front += 1
            max_volume = max(max_volume, height*(tail-front+1))

        return max_volume
