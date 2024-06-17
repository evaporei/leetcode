class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = 0

        def iterate(i: int, money: int) -> int:
            if i >= len(nums):
                return money
            a = iterate(i + 2, money + nums[i])
            b = iterate(i + 3, money + nums[i])
            nonlocal max_money
            max_money = max(max_money, a, b)
            return max_money

        iterate(0, 0)
        iterate(1, 0)

        return max_money
