defmodule Solution do
  @spec is_anagram(s :: String.t, t :: String.t) :: boolean
  def is_anagram(s, t) do
    Enum.sort(String.to_charlist(s)) == Enum.sort(String.to_charlist(t))
  end
end
