class Solution(object):
    def twoSum(self, nums, target):
        vistos = {}
        for i, x in enumerate(nums):
            complet = target - x
            if(complet in vistos):
                resposta = [vistos[complet],i]
                return resposta
            vistos[x] = i
        return None