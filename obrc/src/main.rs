use std::path::Path;
use std::io:: {BufRead, BufReader};
use std::io::prelude::*;
use std::fs::File;
use std::io;
fn main() {
    let path = Path::new("../measurements.txt");
    println!("{}" , path.display());
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let mut buffer = String::new();
    for line in reader.lines() {
        let line = line?;
        println!("{}", line);
    }
    println!("Hello, world!");
}
