defmodule Solution do
  @spec contains_duplicate(nums :: [integer]) :: boolean
  def contains_duplicate(nums) do
    Enum.uniq(nums) |> length != length(nums)
  end
end
