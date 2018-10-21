import itertools

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        return list(itertools.permutation(nums))
        """
        nums.sort()
        l = list()
        l.append(list(nums))
        while self.next_permutation(nums):
            l.append(list(nums))
        return l

    def next_permutation(self, a):
        lt = len(a) - 1
        if lt <= 0:
            return False
        for i in range(lt-1, -1, -1):
            if a[i+1] > a[i]:
                break
        for j in range(lt, 0, -1):
            if a[j] > a[i]:
                a[i], a[j] = a[j], a[i]
                a[i+1:] = a[:i:-1]
                return True
        a.reverse()
        return False

