from math import floor
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        j = len(s) - 1
        for i in range (len(s)//2):
            print(s[i], s[j])
            if s[i] != s[j-i]:
                return False
        return True

        

        