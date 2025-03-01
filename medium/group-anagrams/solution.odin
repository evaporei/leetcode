package group_anagrams

import "core:slice"
import "core:testing"
import "core:fmt"
import "core:sort"

Counter :: [26]u8

counter_of_str :: proc (s: string) -> (c: Counter) {
    for ch in s do c[ch - 'a'] += 1
    return
}

counter_hash :: proc (c: Counter) -> (h: int) {
    for i in 0..<26 {
        h |= int(c[i]) << uint(i);
    }
    return
}

group_anagrams :: proc (strs: []string) -> [][]string {
    groups := make(map[int][dynamic]string)
    defer delete(groups)
    for s in strs {
        h := counter_hash(counter_of_str(s))
        if !(h in groups) do groups[h] = make([dynamic]string)
        append(&groups[h], s)
    }

    result := make([][]string, len(groups))
    i := 0
    for _key, value in groups {
        result[i] = slice.clone(value[:])
        delete(value)
        i += 1
    }
    return result
}

@(test)
group_anagrams_test :: proc (t: ^testing.T) {
    Test_Case :: struct {
        strs: []string,
        groups: [][]string,
    }
    cases := []Test_Case {
        Test_Case{
            strs = []string{"eat","tea","tan","ate","nat","bat"},
            groups = [][]string{[]string{"bat"},[]string{"nat","tan"},[]string{"ate","eat","tea"}},
        },
        Test_Case{
            strs = []string{""},
            groups = [][]string{[]string{""}},
        },
        Test_Case{
            strs = []string{"a"},
            groups = [][]string{[]string{"a"}},
        },
    }

    for i in 0..<len(cases) {
        groups := group_anagrams(cases[i].strs)
        defer delete(groups)
        defer for group in groups do delete(group)

        // conversion because of stupid leetcode types
        groups_set := make(map[int]map[string]struct{})
        defer delete(groups_set)
        for group in groups {
            for word in group {
                counter := counter_of_str(word)
                c_hash := counter_hash(counter)
                if !(c_hash in groups_set) do groups_set[c_hash] = make(map[string]struct{})
                rf := &groups_set[c_hash]
                rf[word] = {}
            }
        }

        expected_groups_set := make(map[int]map[string]struct{})
        defer delete(expected_groups_set)
        for expected_group in cases[i].groups {
            for word in expected_group {
                counter := counter_of_str(word)
                c_hash := counter_hash(counter)
                if !(c_hash in expected_groups_set) do expected_groups_set[c_hash] = make(map[string]struct{})
                rf := &expected_groups_set[c_hash]
                rf[word] = {}
            }
        }

        testing.expect(t, len(groups_set) == len(expected_groups_set), fmt.tprintf("%v expected: %v, got: %v", cases[i].strs, cases[i].groups, groups))

        for k, words in expected_groups_set {
            testing.expect(t, k in groups_set, fmt.tprintf("%v expected: %v, got: %v", cases[i].strs, cases[i].groups, groups))
            for word, _v in words {
                testing.expect(t, word in groups_set[k], fmt.tprintf("%v expected: %v, got: %v", cases[i].strs, cases[i].groups, groups))
            }
        }

        for _k, group in groups_set do delete(group)
        for _k, expected_group in expected_groups_set do delete(expected_group)
    }
}
