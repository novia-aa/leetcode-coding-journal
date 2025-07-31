class Solution:

    def encode(self, strs: List[str]) -> str:
        # Each string is prefixed with its length and a '#'
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the position of the next '#' to get the length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1  # move past the '#'
            res.append(s[i:i + length])
            i += length
        return res
