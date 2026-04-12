class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums) # o(n) 

        # check if the number is start of sequence
        seq_start = set()
        for num in nums: 
            if num-1 not in set():
                seq_start.add(num)
        
        longest = 0
        # seq_start = 
        for num in seq_start:
            count = 1
            while num+count in nums:
                count += 1
            longest = max(longest, count)
        
        return longest


            
