package two_sum

import "core:slice"
import "core:testing"
import "core:fmt"
import "core:sort"

Pair :: struct {
    idx: int,
    value: int,
}

two_sum :: proc (nums: []int, target: int) -> [2]int {
    pairs := make([]Pair, len(nums))
    defer delete(pairs)
    for n, i in nums do pairs[i] = Pair{idx = i, value = n}
    slice.sort_by_key(pairs, proc(p: Pair) -> int { return p.value })

    i, j := 0, len(nums) - 1
    for i < j {
        if pairs[i].value + pairs[j].value > target do j -= 1
        else if pairs[i].value + pairs[j].value < target do i += 1
        else {
            return {pairs[i].idx, pairs[j].idx}
        }
    }

    // // must have one solution
    // unreachable() // can't use because of defer delete()
    return {-1, -1}
}

@(test)
two_sum_test :: proc (t: ^testing.T) {
    Test_Case :: struct {
        nums: []int,
        target: int,
        result: [2]int,
    }
    cases := []Test_Case {
        Test_Case{
            nums = []int{2,7,11,15},
            target = 9,
            result = [2]int{0,1},
        },
        Test_Case{
            nums = []int{3,2,4},
            target = 6,
            result = [2]int{1,2},
        },
        Test_Case{
            nums = []int{3,3},
            target = 6,
            result = [2]int{0,1},
        },
    }

    for i in 0..<len(cases) {
        testing.expect(t, two_sum(cases[i].nums, cases[i].target) == cases[i].result, fmt.tprintf("%v %v, expected: %v", cases[i].nums, cases[i].target, cases[i].result))
    }
}
