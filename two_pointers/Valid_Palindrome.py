class Solution(object):
    def isPalindrome(self, s):
        lista = []
        s = s.lower()
        lista.extend(s)
        #divide a string letra por letra
        # [roblox] -> ["r", "o", "b", "l", "o", "x"]
        right = len(s) -1
        left = 0
        mid = right // 2

        while left < right:
            if not lista[left].isalnum():
                left = left + 1
                continue
            if not lista[right].isalnum():
                right = right - 1
                continue

            if(lista[left] == lista[right]):
                right = right - 1
                left = left + 1
                continue
            else:
                return False
        return True
        