use std::collections::HashMap;
use std::io;

use anyhow::Context;
use anyhow::Result;
use regex::Regex;

fn main() -> Result<()> {
    let mut stdin = io::stdin().lines();

    let instruction_sequence: String = stdin.next().expect("")?;
    stdin.next();

    let mut map: HashMap<String, (String, String)> = HashMap::new();
    let re = Regex::new(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")?;
    for line in stdin {
        let line = line?;
        let (_, [from, to_left, to_right]) = re.captures(&line).context("capture line")?.extract();
        map.insert(
            from.to_string(),
            (to_left.to_string(), to_right.to_string()),
        );
    }

    let mut current: &str = "AAA";

    for (i, instruction) in instruction_sequence.chars().cycle().enumerate() {
        let options = map.get(current).context("asdf")?;
        current = match instruction {
            'L' => &options.0,
            'R' => &options.1,
            _ => anyhow::bail!("unsupported character"),
        };
        if current == "ZZZ" {
            println!("{}", i + 1);
            return Ok(());
        }
    }
    Ok(())
}
