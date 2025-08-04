class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        resposta = [1] * n 
        
        prefix = 1
        for i in range(n):
            resposta[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in reversed(range(n)):
            resposta[i] *= suffix
            suffix *= nums[i]
        
        return resposta
        