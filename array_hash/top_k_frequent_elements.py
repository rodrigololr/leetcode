class Solution(object):
    def topKFrequent(self, nums, k):
        hash = {}

        #conta quantas vezes cada número aparece
        for n in nums:
            hash[n] = hash.get(n, 0) + 1

        #ordena os itens do dicionário pela frequência (do maior para o menor)
        ordenado = sorted(hash.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in ordenado[:k]]
        