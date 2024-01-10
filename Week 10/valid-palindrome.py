class Solution:
    def palindrom_recursion(self,l,r,new_str):
        if(l >= r):
            return True
        if new_str[l] == new_str[r]:            
            return self.palindrom_recursion(l + 1, r - 1, new_str)
        return False
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                i = i.lower()
                new_str += i        
        return self.palindrom_recursion(0,len(new_str)-1,new_str)

        