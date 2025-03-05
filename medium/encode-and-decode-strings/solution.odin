package encode_and_decode_strings

import "core:slice"
import "core:testing"
import "core:fmt"
import "core:sort"
import "core:strings"
import "core:strconv"

SEPARATOR :: "#"
USUAL_LEN :: 2 // digits
EXTRA_CAP :: 50

encode :: proc (input: []string) -> string {
    b_cap := slice.reduce(input, 0, proc(acc: int, curr: string) -> int { return acc + len(curr) + len(SEPARATOR) + USUAL_LEN })
    b := strings.builder_make_len_cap(0, b_cap + EXTRA_CAP)

    for s in input {
        strings.write_uint(&b, len(s))
        strings.write_string(&b, SEPARATOR)
        strings.write_string(&b, s)
    }

    return strings.to_string(b)
}

ARBITRARY_MULT :: 5

decode :: proc (encoded: string) -> []string {
    decoded := make([dynamic]string, 0, len(encoded) * ARBITRARY_MULT)
    i := 0
    for i < len(encoded) {
        j := i
        for encoded[j] != SEPARATOR[0] do j += 1
        s_len, _ := strconv.parse_uint(encoded[i:j])
        j += 1 // SEPARATOR
        s := encoded[j:j+int(s_len)]
        append(&decoded, s)
        i = j + int(s_len)
    }
    return decoded[:]
}

@(test)
encode_and_decode_test :: proc (t: ^testing.T) {
    Test_Case :: struct {
        input: []string,
    }
    cases := []Test_Case {
        Test_Case{
            input = []string{"neet","code","love","you"},
        },
        Test_Case{
            input = []string{"we","say",":","yes"},
        },
    }

    for i in 0..<len(cases) {
        encoded := encode(cases[i].input)
        defer delete(encoded)
        decoded := decode(encoded)
        defer delete(decoded)
        testing.expect(t, slice.equal(decoded, cases[i].input), fmt.tprintf("expected: %v, got: %v, encoded btw: %v", cases[i].input, decoded, encoded))
    }
}
