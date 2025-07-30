class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # to see if duplicated exist, build a hesh table
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
