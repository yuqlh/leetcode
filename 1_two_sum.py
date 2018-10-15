class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mmp = dict()
        for i in range(len(nums)):
            mmp[nums[i]] = i

        for i in range(len(nums)):
            other = mmp.get(target-nums[i], -1)
            if other!=-1 and other!=i:
                return [i, other]
