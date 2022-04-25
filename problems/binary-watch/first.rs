const fn generate_const() -> [i32; 0b1111_111111] {
    let mut result = [0; 0b1111_111111];

    let mut i = 0b0000_000000;
    while i < 0b1111_111111 {
        result[i] = i as i32;
        i += 1;
    }

    result
}

#[inline(always)]
fn generate_time_str(h: i32, m: i32) -> String {
    let hours = format!("{:0<1}", h);
    let minutes = format!("{:0>2}", m);
    format!("{hours}:{minutes}")
}

#[inline(always)]
fn generate_h_m(time: i32) -> (i32, i32) {
    let hours = time >> 6;
    let minutes = time & 0b111111;
    (hours, minutes)
}

#[inline(always)]
fn is_valid_hour(hours: u32) -> bool {
    hours <= 11
}

#[inline(always)]
fn is_valid_minute(minutes: u32) -> bool {
    minutes <= 59
}

#[inline(always)]
fn is_valid_time(time: i32) -> bool {
    let hours = time >> 6;
    let minutes = time & 0b111111;
    is_valid_hour(hours as u32) && is_valid_minute(minutes as u32)
}

#[inline(always)]
fn cmp_count_ones(n: i32, turned_on: i32) -> bool {
    n.count_ones() == turned_on as u32
}

const POSSIBILITIES: [i32; 0b1111_111111] = generate_const();

impl Solution {
    /// turnedOn = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #[inline(always)]
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        match turned_on {
            // Invalid -> can't represent valid time with this many lights turned on
            9 | 10 => vec![],
            0 => vec!["0:00".into()],
            1..=8 => {
                let result: Vec<String> = POSSIBILITIES
                    .into_iter()
                    .filter(|&n| cmp_count_ones(*n, turned_on))
                    .filter(|&n| is_valid_time(*n))
                    .map(|&n| generate_h_m(n))
                    .map(|(h, m)| generate_time_str(h, m))
                    .collect();
                result
            }
            _ => unreachable!(),
        }
    }
}
