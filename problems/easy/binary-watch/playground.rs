#![allow(unused)]

fn sort<T: Ord>(mut v: Vec<T>) -> Vec<T> {
    v.sort();
    v
}

#[inline(always)]
fn bit_count(mut num: i32) -> i32 {
    let mut count = 0;

    while num != 0 {
        count += 1;
        num &= (num - 1);
    }

    count
}

#[inline(always)]
/// turnedOn = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
fn read_binary_watch(turned_on: i32) -> Vec<String> {
    let mut result = vec![];

    for h in 0..12 {
        for m in 0..60 {
            if bit_count(h) + bit_count(m) == turned_on {
                result.push(format!("{:0<1}:{:0>2}", h, m))
            }
        }
    }

    result
}

#[test]
fn turned_on_0() {
    assert_eq!(read_binary_watch(0), vec!["0:00"]);
}

#[test]
fn turned_on_1() {
    // all
    assert_eq!(
        sort(read_binary_watch(1)),
        sort(vec![
            "0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"
        ])
    );
    // // just hours
    // assert_eq!(sort(read_binary_watch(1)), sort(vec!["1:00", "2:00", "4:00", "8:00"]));
    // // just minutes
    // assert_eq!(
    //     read_binary_watch(1),
    //     vec!["0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    // );
}

#[test]
fn turned_on_2() {
    // all
    assert_eq!(
        sort(read_binary_watch(2)),
        sort(vec![
            "0:03", "0:05", "0:06", "0:09", "0:10", "0:12", "0:17", "0:18", "0:20", "0:24", "0:33",
            "0:34", "0:36", "0:40", "0:48", "1:01", "1:02", "1:04", "1:08", "1:16", "1:32", "2:01",
            "2:02", "2:04", "2:08", "2:16", "2:32", "3:00", "4:01", "4:02", "4:04", "4:08", "4:16",
            "4:32", "5:00", "6:00", "8:01", "8:02", "8:04", "8:08", "8:16", "8:32", "9:00",
            "10:00"
        ])
    );
    // // just hours
    // assert_eq!(read_binary_watch(1), vec!["1:00", "2:00", "4:00", "8:00"]);
    // // just minutes
    // assert_eq!(
    //     read_binary_watch(1),
    //     vec!["0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    // );
}

#[test]
fn turned_on_9() {
    assert_eq!(read_binary_watch(9), Vec::<String>::new());
}
