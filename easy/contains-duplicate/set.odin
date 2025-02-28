package contains_duplicate

import "core:slice"
import "core:testing"
import "core:fmt"

contains_duplicates :: proc (nums: []int) -> bool {
    // could be bool
    s := make(map[int]struct{})
    defer delete(s)
    for n in nums {
        if n in s {
            return true
        }
        s[n] = {}
    }
    return false
}

Test_Case :: struct {
    nums: []int,
    duplicates: bool,
}

@(test)
contains_duplicates_test :: proc (t: ^testing.T) {
    cases := []Test_Case {
        Test_Case{
            nums = []int{1,2,3,1},
            duplicates = true,
        },
        Test_Case{
            nums = []int{1,2,3,4},
            duplicates = false,
        },
        Test_Case{
            nums = []int{1,1,1,3,3,4,3,2,4,2},
            duplicates = true,
        },
        Test_Case{
            nums = []int{1,5,-2,-4,0},
            duplicates = false,
        },
    }

    for i in 0..<len(cases) {
        testing.expect(t, contains_duplicates(cases[i].nums) == cases[i].duplicates, fmt.tprintf("%v", cases[i].nums))
    }
}
