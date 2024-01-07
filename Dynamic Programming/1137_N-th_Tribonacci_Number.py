class Solution:

    
    def tribonacci(self, n: int) -> int:

        t0, t1, t2 = 0, 1, 1
        tribonacci = [t0, t1, t2]

        for i in range(3, n+1):
            tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3])

        return tribonacci[n]

        
        