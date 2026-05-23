class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #creates a dict where every key starts with an empty list
        for s in strs: 
            sorted_s = sorted(s) #"tea" -> ['a', 'e', 't']            sorted_list = ''.join(sorted_s)
            sortedS = ''.join(sorted_s) # ['a', 'e', 't'] -> "aet"
            res[sortedS].append(s) 
        return list(res.values())