class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0

        for num in nums:
            for i in nums:
                if (num == i):
                    count += 1

            if (count > 1):
                return True

            count = 0

        return False