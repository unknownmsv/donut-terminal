use std::process::Command;
use crate::ai;

pub async fn run_command(cmd: &str) {
    if cmd.starts_with("ai:") || cmd.starts_with("ai ") {
        let prompt = cmd.splitn(2, ':').nth(1).unwrap_or("").trim();
        let res = ai::ask_ai(prompt).await;
        println!("[AI 🧠]: {}", res);
        return;
    }

    let output = Command::new("sh")
        .arg("-c")
        .arg(cmd)
        .output();

    match output {
        Ok(output) => {
            if !output.stdout.is_empty() {
                print!("{}", String::from_utf8_lossy(&output.stdout));
            }
            if !output.stderr.is_empty() {
                eprint!("[!] {}", String::from_utf8_lossy(&output.stderr));
            }
        }
        Err(e) => {
            println!("[!] Failed to execute command: {}", e);
        }
    }
}
