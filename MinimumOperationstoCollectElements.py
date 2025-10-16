class Solution(object):
    def minOperations(self, nums, k):
        # tá então já sei bem oq fazer
        # percorro o arr inverso, depois disso eu preciso criar uma lista onde nessa lista eu precis ter, 1, 2 e k PELO MENOS
        # quando já tiver esses três, ai vapo
        coletado = set()
        preciso = set(range(1,k+1))
        oper = 0
        for i in reversed(nums):
            if(i in preciso):
                coletado.add(i)
            oper += 1
            if(coletado == preciso):
                return oper
        return -1 
           

        