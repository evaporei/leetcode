# counting-bits

1. `i % 2` == `i & 1`; Because a number is odd when the last bit is 1. Usually it's slower (unless --release), but here it allows to solve the problem in O(n);
2. `i / 2` is an optimization that gets the count of bits for the number that's half of the current one, then you just count the last bit. Eg: for `6` or `7`, it will have the same bit count as `3` + if it's odd.
