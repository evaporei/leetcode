defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    pairs = nums
    |> Enum.with_index
    |> Enum.sort_by(&(elem(&1, 0)))

    Enum.reduce(pairs, {0, length(nums) - 1, []}, fn (_curr, {i, j, l}) ->
        {i_val, i_idx} = Enum.at(pairs, i)
        {j_val, j_idx} = Enum.at(pairs, j)
        cond do
            i_val + j_val > target -> {i, j - 1, l}
            i_val + j_val < target -> {i + 1, j, l}
            true -> {i, j, [i_idx, j_idx]}
        end
    end)
    |> elem(2)
  end
end
