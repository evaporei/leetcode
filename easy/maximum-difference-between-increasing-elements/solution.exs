defmodule Solution do
  @spec maximum_difference(nums :: [integer]) :: integer
  def maximum_difference(nums) do
    [r, m] = Enum.reduce(nums, [-1, 2305843009213693951], fn curr, [res, min_so_far] ->
      min_so_far = min(min_so_far, curr)
      if curr > min_so_far do
        [max(res, curr - min_so_far), min_so_far]
      else
        [res, min_so_far]
      end
    end)
    r
  end
end
