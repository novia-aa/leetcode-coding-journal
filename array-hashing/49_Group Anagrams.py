class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)  # 如果 key 不在字典中，则自动插入一个空列表
        for s in strs:
            sorted_s = ''.join(sorted(s))  # 把 s 排序，作为哈希表的 key
            d[sorted_s].append(s)  # 排序后相同的字符串分到同一组
        return list(d.values())  # 哈希表的 value 保存分组后的结果



"""
anagrams 可以看成两个字符串从小到大排序后相等，那么两个字符串就互为字母异位词，否则不是
"""
        
