package contains_duplicate

import "core:slice"
import "core:testing"
import "core:fmt"
import "core:sort"

is_anagram_counter :: proc (t: string, s: string) -> bool {
    t_counter := make(map[u8]int)
    defer delete(t_counter)
    for i in 0..<len(t) {
        ch := t[i]
        if ch in t_counter {
            t_counter[ch] += 1
        } else {
            t_counter[ch] = 1
        }
    }

    s_counter := make(map[u8]int)
    defer delete(s_counter)
    for i in 0..<len(t) {
        ch := s[i]
        if ch in s_counter {
            s_counter[ch] += 1
        } else {
            s_counter[ch] = 1
        }
    }
    
    for key, _value in t_counter do if t_counter[key] != s_counter[key] do return false
    for key, _value in s_counter do if s_counter[key] != t_counter[key] do return false
    return true
}

is_anagram_counter2 :: proc (t: string, s: string) -> bool {
    counter := make(map[u8]int)
    defer delete(counter)
    for i in 0..<len(t) {
        ch := t[i]
        if ch in counter {
            counter[ch] += 1
        } else {
            counter[ch] = 1
        }
    }
    for i in 0..<len(s) {
        ch := s[i]
        if ch in counter {
            counter[ch] -= 1
        } else {
            return false
        }
    }
    
    for _key, value in counter do if value != 0 do return false
    return true
}

@(test)
is_anagram_counter_test :: proc (t: ^testing.T) {
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
        testing.expect(t, is_anagram_counter(cases[i].t, cases[i].s) == cases[i].anagram, fmt.tprintf("%v %v, expected: %v", cases[i].t, cases[i].s, cases[i].anagram))
        testing.expect(t, is_anagram_counter2(cases[i].t, cases[i].s) == cases[i].anagram, fmt.tprintf("%v %v, expected: %v", cases[i].t, cases[i].s, cases[i].anagram))
    }
}
