class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucketsort
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 1 
            else:
                counts[i] += 1 
        
        freq = {}
        maxfreq = 0
        for i in counts:
            f = counts[i]
            if f not in freq:
                freq[f] = [i]
            else:
                freq[f].append(i)
            
            if f > maxfreq:
                maxfreq = f
        
        vals = []
        while k > 0:
            while maxfreq not in freq:
                maxfreq -= 1
            vals.extend(freq[maxfreq])
            
            k -= len(freq[maxfreq])
            maxfreq -=1

        return vals
            
        

