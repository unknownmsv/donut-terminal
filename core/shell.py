import os
import getpass
from core.commands import run_command, load_donut_lang, open_with_editor

class DonutShell:
    def __init__(self):
        self.super_user = False
        self.username = getpass.getuser()
        self.cwd = os.getcwd()
        load_donut_lang()

    def run(self):
        os.system("clear")
        print("Welcome to Donut Terminal [Mobile Edition]")

        while True:
            prefix = "o$" if self.super_user else "$"
            try:
                command = input(f"{self.username} {prefix} ").strip()

                if command in ["exit", "quit"]:
                    print("Goodbye!")
                    break

                if command == "o$":
                    self.super_user = not self.super_user
                    continue

                if command.startswith("cd "):
                    path = command.split(" ", 1)[1]
                    try:
                        os.chdir(path)
                        self.cwd = os.getcwd()
                    except FileNotFoundError:
                        print(f"No such directory: {path}")
                    continue

                if command.startswith("donutTTE"):
                    parts = command.split(" ", 1)
                    if len(parts) == 1 or not parts[1].strip():
                        print("[!] لطفاً نام فایل را وارد کنید. مثال: donutTTE file.txt")
                    else:
                        filename = parts[1].strip()
                        open_with_editor(filename)
                    continue

                run_command(command, self.super_user, self.cwd)

            except KeyboardInterrupt:
                print("\nUse 'exit' to quit.")