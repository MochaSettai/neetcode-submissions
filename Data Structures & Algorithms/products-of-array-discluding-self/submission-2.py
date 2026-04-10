# My initial solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0

        for n in nums:
            if n == 0:
                count += 1

        # Get the product
        if count == 1:
            for n in nums:
                if n != 0:
                    product *= n
        else:
            for n in nums:
                product *= n
        
        res = []

        for i in range(len(nums)):
            if count > 1:
                res.append(0)
            elif count == 0:
                res.append(int(product / nums[i]))
            else:
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(product)
        
        return res