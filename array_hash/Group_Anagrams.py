class Solution(object):
    def groupAnagrams(self, strs):
        grupos = defaultdict(list)
        for palavra in strs:
            # ordena as letras da palavra e transforma em tupla para usar como chave
            chave = tuple(sorted(palavra))
            # adiciona a palavra ao grupo correspondente à chave
            grupos[chave].append(palavra)
        return list(grupos.values())