class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        #pass 1: move the entire array over
        for i in range(n):
            ans[i] = nums[i]
        
        #pass 2 : now add the same element array over
        for i in range(n):
            ans[i + n] = nums[i]

        return ans

sol = Solution()
result = sol.getConcatenation([22,21,20,21])
print(result)
