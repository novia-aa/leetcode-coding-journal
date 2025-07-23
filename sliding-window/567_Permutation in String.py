class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            if len(s1) > len(s2):
                return False
            
            s1_count = Counter(s1)
            window = Counter(s2[:len(s1)])
            if window == s1_count:
               return True

            for i in range(len(s1), len(s2)):
                window[s2[i]] += 1
                window[s2[i - len(s1)]] -= 1

                # 清除計數為 0 的項目，否則 Counter 無法判斷相等
                if window[s2[i - len(s1)]] == 0:
                    del window[s2[i - len(s1)]]

                if window == s1_count:
                    return True

            return False


    """
    解題關鍵: 所有排列的字元組成一樣，所以 比較字元出現頻率是否相同即可
    """
