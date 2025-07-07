class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase all the words
        s = s.lower() 
        # build forward and backward pointer
        forward = 0 
        backward = len(s)-1
        # iterate the list until forward> backward
        # check if s[forward] is the same as s[backward] 
        while forward < backward:
            # if it is not alpha number then sikp
            while forward < backward and not s[forward].isalnum():
                forward += 1
            while forward < backward and not s[backward].isalnum():
                backward -= 1
            if s[forward] != s[backward]:
                return False 
            forward +=1
            backward -=1
            
        
        return True

        
