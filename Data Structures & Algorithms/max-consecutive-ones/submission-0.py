class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_count = 0
        for i in range (0,len(nums)):
            if nums[i] != 0:
                current_count +=1
            else:
                current_count = 0

            if current_count >= max_count:
                max_count = current_count

        return max_count



        