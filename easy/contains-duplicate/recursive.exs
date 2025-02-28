defmodule Solution do
  @spec contains_duplicate(nums :: [integer]) :: boolean
  def contains_duplicate(nums), do: nums |> Enum.sort |> cd()
  def cd([]), do: false
  def cd([elem]), do: false
  def cd([h | t]) do
    if h == hd(t) do
      true
    else
      cd(t)
    end
  end
end
