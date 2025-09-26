class Solution:
    def isPalindrome(self, s: str) -> bool:
        def rec(l,r):
            if l>=r:
                return True
            if not s[l].isalnum():
                return rec(l+1,r)
            if not s[r].isalnum():
                return rec(l,r-1)
            
            if s[l].lower() != s[r].lower():
                return False
            
            return rec(l+1,r-1)
        
        
        return rec(0, len(s)-1)

        