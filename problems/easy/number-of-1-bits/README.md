# number-of-1-bits

1. `1` is definitely less verbose than `0b000000000000000000000000000000000001`;
2. There's no need for an `if` if you always compare the first bit and leverage that for the `weight` count;
3. You can save one variable if you mutate the input.
