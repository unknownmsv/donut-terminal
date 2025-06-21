use std::process::Command;

fn main() {
    println!("🚀 Starting Donut Terminal...");

    let status = Command::new("python3")
        .arg("main.py")
        .status()
        .expect("Failed to launch main.py");

    if status.success() {
        println!("✅ Donut Terminal exited successfully.");
    } else {
        eprintln!("❌ Donut Terminal crashed or exited with error.");
    }
}