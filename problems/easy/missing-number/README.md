# missing-number

1. Sorting can ease on the iteraton to find the missing number by making every element match `i`;
2. Window pairs can be used to compare `i` and `i + 1` to see if the difference shows where the missing number is;
3. Sorting is usually O(n log n), creating a HashSet is O(n) and doing a `.contains` is also O(1), so this is faster;
4. XOR has the commutative and associative property; Doing XOR with the same number, eg: `101 ^ 101` gives `0` as result; So the missing number will be the reminder of doing a XOR of all elements (+ `i` in the iteration);
5. `n * (n + 1) / 2` is equivalent to doing a sum of all numbers in a range.
