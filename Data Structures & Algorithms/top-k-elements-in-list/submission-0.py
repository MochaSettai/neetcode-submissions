class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        output = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for i in range(k):
            top = max(freq, key = freq.get)
            output.append(top)
            del freq[top]
        
        return output