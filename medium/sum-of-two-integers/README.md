# sum-of-two-integers

Binary sheet cheat: https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently.

1. `a ^ b` is equal to the sum without carrying (when two 1s go to the next "slot");
2. `(a & b) << 1` is equal to the carrying part of the sum, because we only keep values that are both 1s (AND), then shift it to the correct slot;
3. Either loop or recursion can be used to apply the operations above multiple times.
