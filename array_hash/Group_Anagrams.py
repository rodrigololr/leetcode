class Solution(object):
    def groupAnagrams(self, strs):
        grupos = defaultdict(list)
        for palavra in strs:
            chave = tuple(sorted(palavra))
            grupos[chave].append(palavra)
        
        return list(grupos.values())
        