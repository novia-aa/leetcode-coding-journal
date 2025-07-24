class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort the list first
        piles.sort()
        # store the value
       
        # find the mid point
        front, tail = 1, max(piles) # the worst case, eat the maximun in a time
        result = tail
        while front <= tail:
            mid = (front + tail) // 2
            # calculate how many hours taken
            tmp_h=0
            for i in range(len(piles)):
                tmp_h += math.ceil(piles[i] / mid)
        # if the tmp_h < h,  try smaller number
            if tmp_h <= h:
                tail = mid-1
                result = mid
        # if the tmp_h > h,  try larger number
            elif tmp_h > h:
                front = mid+ 1
        return result

  """
    如何知道該用「二分答案」,類型特徵
    - 你要找某個數值的最小值或最大值
    - 有一個“條件判斷函數”f(x)，你可以用它來驗證「這個 x 可不可以」
    - 當 x 越大 / 越小時，條件的結果是單調的（monotonic）
    """
