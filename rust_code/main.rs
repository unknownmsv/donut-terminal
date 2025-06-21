use std::process::Command;
use std::path::Path;

fn main() {
    println!("🚀 Trying to launch Donut Terminal...");

    let terminal_commands = vec![
        ("xterm", vec!["-e", "python3 main.py"]),
        ("gnome-terminal", vec!["--", "python3", "main.py"]),
        ("konsole", vec!["-e", "python3", "main.py"]),
        ("xfce4-terminal", vec!["-e", "python3 main.py"]),
        ("lxterminal", vec!["-e", "python3 main.py"]),
        ("kitty", vec!["python3", "main.py"]),
        ("alacritty", vec!["-e", "python3", "main.py"]),
        ("tilix", vec!["-e", "python3", "main.py"]),
    ];

    for (terminal, args) in terminal_commands {
        if which(terminal) {
            let status = Command::new(terminal)
                .args(&args)
                .status();

            match status {
                Ok(status) if status.success() => {
                    println!("✅ Launched successfully with {}", terminal);
                    return;
                }
                Ok(_) => {
                    println!("⚠️ Failed to run with terminal: {}", terminal);
                }
                Err(e) => {
                    println!("❌ Error running {}: {}", terminal, e);
                }
            }
        }
    }

    eprintln!("🚫 No supported terminal emulator found. Please install one (e.g., xterm or gnome-terminal).");
}

/// بررسی اینکه آیا باینری مورد نظر در مسیر PATH هست یا نه
fn which(program: &str) -> bool {
    std::env::var("PATH")
        .unwrap_or_default()
        .split(':')
        .any(|p| Path::new(p).join(program).exists())
}