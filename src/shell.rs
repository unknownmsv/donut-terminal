use std::io::{self, Write};
use std::env;
use crate::commands;

pub async fn run() {
    println!("Welcome to Donut Terminal [Rust Edition]");
    let mut super_user = false;

    loop {
        print!("{} {} ", whoami::username(), if super_user { "o$" } else { "$" });
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let command = input.trim();

        match command {
            "exit" | "quit" => {
                println!("Goodbye!");
                break;
            }
            "o$" => {
                super_user = !super_user;
            }
            cmd if cmd.starts_with("cd ") => {
                let path = cmd.strip_prefix("cd ").unwrap_or("/");
                if let Err(e) = env::set_current_dir(path) {
                    println!("[!] No such directory: {}", e);
                }
            }
            _ => {
                commands::run_command(command).await;
            }
        }
    }
}
