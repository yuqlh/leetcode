class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        tmp = self.powf(x, abs(n))
        #print(tmp)
        return tmp if n>=0 else 1.0/tmp


    def powf(self, x, n):
        if n==0:
            return 1
        ye = 1
        re = x
        while n>1:
            if n&1:
                ye *= re
            re *= re
            n //= 2
        return re*ye

    def powf2(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        #print(x, n)
        tmp = self.powf(x, n//2)
        #print(tmp)
        return tmp*tmp if n%2==0 else tmp*tmp*x

