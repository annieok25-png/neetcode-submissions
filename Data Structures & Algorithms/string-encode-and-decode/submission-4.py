class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for i in strs: 
            parts.append(f"{len(i)}#{i}")
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i <len(s): 
            j = i 
            while s[j] != "#": 
                j += 1 #if the number is one digit, j is 1 as "#" is in index 1
            length = int (s[i:j]) #length of number + #
            start = j+ 1 
            end = start + length 
            res.append(s[start:end])
            i = end
        return res


