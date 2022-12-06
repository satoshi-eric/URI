use std::io;

fn get_month_name_by_number(month_number: i32) -> String {
    match month_number {
        1 => String::from("January"),
        2 => String::from("February"),
        3 => String::from("March"),
        4 => String::from("April"),
        5 => String::from("May"),
        6 => String::from("June"),
        7 => String::from("July"),
        8 => String::from("August"),
        9 => String::from("September"),
        10 => String::from("October"),
        11 => String::from("November"),
        12 => String::from("December"),
        _ => String::from("")
    }
}

fn get_input() -> i32 {
    let mut month_number: String = String::new();
    io::stdin().read_line(&mut month_number).expect("Digite sua renda");
    let month_number: i32 = month_number.trim().parse().expect("Problema ao converter entrada");
    return month_number;
}

fn main() {
    let month_number = get_input();
    let month_name = get_month_name_by_number(month_number);
    println!("{}", month_name);
}