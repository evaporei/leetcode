package contains_duplicate

import "core:slice"
import "core:testing"
import "core:fmt"
import "core:sort"

is_anagram_sort :: proc (t: string, s: string) -> bool {
    t_raw_data := raw_data(t)
    t_slice:[]u8 = make([]u8, len(t))
    defer delete(t_slice)
    for i in 0..<len(t) do t_slice[i] = t_raw_data[i]
    sort.quick_sort(t_slice)

    s_raw_data := raw_data(s)
    s_slice:[]u8 = make([]u8, len(s))
    defer delete(s_slice)
    for i in 0..<len(s) do s_slice[i] = s_raw_data[i]
    sort.quick_sort(s_slice)

    return slice.equal(t_slice, s_slice)
}

@(test)
is_anagram_sort_test :: proc (t: ^testing.T) {
    Test_Case :: struct {
        t: string,
        s: string,
        anagram: bool,
    }
    cases := []Test_Case {
        Test_Case{
            t = "anagram",
            s = "nagaram",
            anagram = true,
        },
        Test_Case{
            t = "rat",
            s = "car",
            anagram = false,
        },
    }

    for i in 0..<len(cases) {
        testing.expect(t, is_anagram_sort(cases[i].t, cases[i].s) == cases[i].anagram, fmt.tprintf("%v %v, expected: %v", cases[i].t, cases[i].s, cases[i].anagram))
    }
}
