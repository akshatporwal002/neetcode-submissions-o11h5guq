from math import ceil

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters_dict = {}
        for letter in s:
            if letter not in letters_dict:
                letters_dict[letter] = 0 
            else:
                letters_dict[letter] += 1
        
        letters_dict_2 = {}
        for letter in t:
            if letter not in letters_dict_2:
                letters_dict_2[letter] = 0 
            else:
                letters_dict_2[letter] += 1
        
        if letters_dict == letters_dict_2:
            return True
        else:
            return False

        return True