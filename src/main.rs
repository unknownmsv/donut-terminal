mod shell;
mod gui;
mod commands;
mod ai;
mod utils;
mod config;

#[tokio::main]
async fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() > 1 && args[1] == "--gui" {
        gui::start_gui();
    } else {
        shell::run().await;
    }
}