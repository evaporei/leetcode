package contains_duplicate

import "core:slice"
import "core:testing"
import "core:fmt"
import vmem "core:mem/virtual"
import "base:runtime"

Node :: struct {
    value: int,
    next: ^Node,
}

NODE_COUNT :: 1000

Set :: struct {
    buckets: [NODE_COUNT]^Node,
    level_arena: vmem.Arena,
    allocator: runtime.Allocator,
}

INVALID_VALUE :: 4000000000

set_init :: proc(s: ^Set) {
	s.allocator = vmem.arena_allocator(&s.level_arena)
    context.allocator = s.allocator
    for &b in s.buckets {
        b = new(Node)
        b.value = INVALID_VALUE
    }
}

set_add :: proc(s: ^Set, n: int) -> bool {
    context.allocator = s.allocator
    idx := abs(n) % NODE_COUNT
    curr := s.buckets[idx]
    for curr.next != nil {
        if curr.value == n do return true
        curr = curr.next
    }
    if curr.value == n do return true
    curr.next = new(Node)
    curr.next.value = n
    return false
}

set_delete :: proc(s: ^Set) {
    free_all(s.allocator)
    // vmem.arena_destroy(&s.level_arena)
}

contains_duplicates :: proc (nums: []int) -> bool {
    set: Set
    set_init(&set)
    defer set_delete(&set)
    for n in nums {
        if set_add(&set, n) {
            return true
        }
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
