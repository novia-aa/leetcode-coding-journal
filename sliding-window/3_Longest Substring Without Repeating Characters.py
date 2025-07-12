class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # without reapeating character --> use hash table to record
        last_seen = {}
        # need a start pointer and max_len to begin
        start, max_len = 0, 0

        # iterate the string
        for i, ch in enumerate(s):
            # check if the chracter in hash or not
                # start at the next index of the dupilcated one
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch] + 1
            # if already exist, count the current length and compare with the max one and delete duplicated one
            # else not keep storing
            last_seen[ch] = i
            max_len = max(max_len, i - start + 1)

        return max_len
            

        
