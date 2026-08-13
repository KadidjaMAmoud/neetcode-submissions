class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seq = []

        if len(nums) > 1:
            a = [nums[0]]
            for x in range(1,len(nums)):
                if nums[x] - a[-1] == 1:
                    a.append(nums[x])
                elif nums[x] - a[-1] > 1: # i want to ignore "== 0"
                    seq.append(len(a))
                    a = [nums[x]]
            seq.append(len(a))
            seq.sort()
            return(seq[-1])
        else:
            return len(nums)