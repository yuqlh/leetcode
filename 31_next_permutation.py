class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.my_next_permutation(nums)

    def my_next_permutation(self, a):
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


