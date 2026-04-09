class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for string in strs:
            # needs a searchable key with frequencies of letters
            key = [0]*26                                            
            for letter in string:                        
                letter_val = ord(letter.lower()) - ord('a')        
                key[letter_val] += 1
            key = tuple(key)
            if key not in table: 
                # add space to append 
                table[key] = []
            table[key].append(string)
        #table.values gives values as iterable but must be wrapped 
        return list(table.values())
        

        
        