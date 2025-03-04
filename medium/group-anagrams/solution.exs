defmodule Solution do
  @spec group_anagrams(strs :: [String.t()]) :: [[String.t()]]
  def group_anagrams(strs) do
    strs
    |> Enum.reduce(%{}, fn s, acc ->
      ch_list = String.to_charlist(s)
      freqs = Enum.frequencies(ch_list)
      Map.update(acc, freqs, [s], fn l -> l ++ [s] end)
    end)
    |> Map.values()
  end
end
