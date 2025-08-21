class Solution(object):
    def isValid(self, s):
        pilha = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():
                pilha.append(char)
            else:
                try:
                    if pilha.pop() != mapping[char]:
                        return False
                except:
                    return False

        return not pilha
        