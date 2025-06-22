use eframe::{egui, App, Frame, NativeOptions};
use std::process::Command;

pub struct DonutApp {
    input: String,
    output: String,
}

impl Default for DonutApp {
    fn default() -> Self {
        Self {
            input: String::new(),
            output: String::from("🍩 Donut Terminal Ready"),
        }
    }
}

impl App for DonutApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut Frame) {
        use egui::{Color32, Visuals};

        // تنظیم حالت شیشه‌ای
        ctx.set_visuals(Visuals {
            window_fill: Color32::from_rgba_unmultiplied(20, 20, 20, 180),
            panel_fill: Color32::from_rgba_unmultiplied(10, 10, 10, 160),
            ..Visuals::dark()
        });

        // تنظیم استایل فونت
        let mut style = (*ctx.style()).clone();
        style.override_text_style = Some(egui::TextStyle::Monospace);
        ctx.set_style(style);

        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("🍩 Donut Terminal");

            ui.separator();

            ui.horizontal(|ui| {
                ui.label("Command:");
                let response = ui.text_edit_singleline(&mut self.input);
                if ui.button("Run").clicked()
                    || (response.lost_focus() && ui.input(|i| i.key_pressed(egui::Key::Enter)))
                {
                    self.output = run_shell(&self.input);
                    self.input.clear();
                }
            });

            ui.separator();
            ui.label("Output:");
            egui::ScrollArea::vertical().show(ui, |ui| {
                ui.code(&self.output);
            });
        });
    }
}

pub fn start_gui() {
    let options = NativeOptions {
        viewport: egui::ViewportBuilder::default()
            .with_inner_size([720.0, 420.0])
            .with_decorations(false)
            .with_title("Donut Terminal GUI".to_owned()), // ← حواست باشه که string می‌خواد
        ..Default::default()
    };

    eframe::run_native(
        "Donut Terminal GUI",
        options,
        Box::new(|_cc| Ok(Box::new(DonutApp::default()))),
    )
    .expect("GUI failed");
}

fn run_shell(cmd: &str) -> String {
    if cmd.trim().is_empty() {
        return "❗ Please enter a command".to_string();
    }

    let result = if cfg!(target_os = "windows") {
        Command::new("cmd").args(["/C", cmd]).output()
    } else {
        Command::new("sh").arg("-c").arg(cmd).output()
    };

    match result {
        Ok(output) => {
            let stdout = String::from_utf8_lossy(&output.stdout);
            let stderr = String::from_utf8_lossy(&output.stderr);
            format!("{stdout}{stderr}")
        }
        Err(e) => format!("❌ Error: {}", e),
    }
}