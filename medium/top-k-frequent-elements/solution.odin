package top_k_frequent_elements

import "core:slice"
import "core:testing"
import "core:fmt"
import "core:sort"

Count :: struct {
    n: int,
    freq: int,
}

top_k_frequent_elements :: proc (nums: []int, k: int) -> []int {
    freq_map := make(map[int]int)
    defer delete(freq_map)
    for n in nums do freq_map[n] += 1

    counts := make([]Count, len(freq_map))
    defer delete(counts)
    i := 0
    for n, freq in freq_map {
        counts[i] = Count{n = n, freq = freq}
        i += 1
    }
    slice.reverse_sort_by_key(counts, proc(count: Count) -> int { return count.freq })
    return slice.mapper(counts, proc(count: Count) -> int { return count.n })[:k]
}

@(test)
top_k_frequent_elements_test :: proc (t: ^testing.T) {
    Test_Case :: struct {
        nums: []int,
        k: int,
        result: []int,
    }
    cases := []Test_Case {
        Test_Case{
            nums = []int{1,1,1,2,2,3},
            k = 2,
            result = []int{1,2},
        },
        Test_Case{
            nums = []int{1},
            k = 1,
            result = []int{1},
        },
    }

    for i in 0..<len(cases) {
        top_k := top_k_frequent_elements(cases[i].nums, cases[i].k)
        defer delete(top_k)
        testing.expect(t, slice.equal(top_k, cases[i].result), fmt.tprintf("%v %v, expected: %v, got: %v", cases[i].nums, cases[i].k, cases[i].result, top_k))
    }
}
