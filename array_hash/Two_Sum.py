class Solution(object):
    def twoSum(self, nums, target):
        vistos = {}
        for i, x in enumerate(nums):
            complet = target - x # calcula o que precisa para chegar ao target
            if(complet in vistos): # verifica se já vimos esse complemento antes
                resposta = [vistos[complet],i]
                return resposta
            vistos[x] = i # DEPOIS da verificação, adiciona o número atual
        return None

