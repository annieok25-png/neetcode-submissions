class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: #parameter is called strs which is a list of strings, output is a list of a list of strings
        res = defaultdict(list)
        for s in strs: 
            sorted_s = sorted(s)
            new_s = "".join(sorted_s)
            res[new_s].append(s)
        return list(res.values())

        
        
        
        
        
        
        
        
        
        






        
        
        
        
        
        
        
        # res = defaultdict(list) #creates a dict where every key starts with an empty list
        # for s in strs: 
        #     sorted_s = sorted(s) #"tea" -> ['a', 'e', 't']            sorted_list = ''.join(sorted_s)
        #     sortedS = ''.join(sorted_s) # ['a', 'e', 't'] -> "aet"
        #     res[sortedS].append(s) 
        # return list(res.values())