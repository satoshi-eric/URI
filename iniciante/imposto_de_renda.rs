use std::io;

fn get_input() -> f64 {
    let mut renda: String = String::new();
    io::stdin().read_line(&mut renda).expect("Digite sua renda");
    let renda: f64 = renda.trim().parse().expect("Problema ao converter entrada");
    return renda;
}

fn calculate_tax(mut income: f64) -> String {
    if income >= 0. && income <= 2000. {
        return String::from("Isento");
    } else if income > 2000. && income <= 3000. {
        let tax_rate: f64 = 0.08;
        income = income - 2000.;
        let tax: f64 = tax_rate * income;
        return String::from(format!("R$ {:.2}", tax));
    } else if income > 3000. && income <= 4500. {
        let mut tax: f64 = 0.;
        let tax_rate: f64 = 0.08;
        tax += 1000. * tax_rate;
        income -= 3000.;
        let tax_rate: f64 = 0.18;
        tax += income * tax_rate;
        return String::from(format!("R$ {:.2}", tax));
    } else if income > 4500. {
        let mut tax: f64 = 0.;
        let tax_rate: f64 = 0.08;
        tax += 1000. * tax_rate;
        let tax_rate: f64 = 0.18;
        tax += 1500. * tax_rate;
        let tax_rate: f64 = 0.28;
        income -= 4500.;
        tax += income * tax_rate;
        return String::from(format!("R$ {:.2}", tax));
    } else {
        return String::new();
    }
}

fn main() {
    let renda: f64 = get_input();
    let tax: String = calculate_tax(renda);
    println!("{}", tax);
}