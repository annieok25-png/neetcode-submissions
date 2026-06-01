class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = dict(zip(")}]", "({[")) #sets closing brackets as the keys as it searches for opening brackets 
        stack = []
        
        for c in s: 
            if c in close_to_open: 
                if stack and stack[-1] == close_to_open[c]: #stack gives false if list is empty 
                    stack.pop() #removes the item at the end of list 
                else: 
                    return False 
            else: 
                stack.append(c)
        return (len(stack) == 0)


        