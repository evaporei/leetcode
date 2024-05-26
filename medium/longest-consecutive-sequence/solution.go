func longestConsecutive(nums []int) int {
    set := map[int]bool{}
    for _, n := range nums {
        set[n] = true
    }
    longest := 0
    for _, n := range nums {
        offset := 1
        // start of sequence
        if !set[n - offset] {
            for set[n + offset] {
                offset += 1
            }
            if offset > longest {
                longest = offset
            }
        }
    }
    return longest
}
