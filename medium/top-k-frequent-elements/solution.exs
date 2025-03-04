defmodule Solution do
  @spec top_k_frequent(nums :: [integer], k :: integer) :: [integer]
  def top_k_frequent(nums, k) do
    nums
    |> Enum.frequencies
    |> Map.to_list
    |> Enum.sort_by(fn {n, freq} -> freq end, :desc)
    |> Enum.map(fn {n, freq} -> n end)
    |> Enum.take(k)
  end
end
