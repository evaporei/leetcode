defmodule Solution do
  @spec is_anagram(s :: String.t, t :: String.t) :: boolean
  def is_anagram(s, t) do
    counter(s) == counter(t)
  end

  # could have used Enum.frequencies
  @spec counter(s :: String.t) :: map()
  def counter(s) do
    Enum.reduce(String.to_charlist(s), %{}, fn ch, acc -> Map.update(acc, ch, 1, &(&1 + 1)) end)
  end
end
