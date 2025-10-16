class Solution(object):
    def generateParenthesis(self, n):
        def dfs(seq, abertos, fechados):
            if len(seq) == 2 * n:
                res.append(seq)
                return

            if abertos < n:
                dfs(seq + "(", abertos + 1, fechados)

            if fechados < abertos:
                dfs(seq + ")", abertos, fechados + 1)

        res = []
        dfs("", 0, 0)
        return res
