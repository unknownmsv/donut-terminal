import os
import re
import subprocess
from time import sleep
from core.ai import ask_ai

donut_lang = {}

def load_donut_lang(path="config/donut.lang"):
    """بارگذاری دستورات سفارشی از فایل پیکربندی"""
    if not os.path.exists(path):
        print(f"[!] فایل زبان یافت نشد: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                left, right = line.strip().split("=", 1)
                donut_lang[left.strip()] = right.strip()

def open_with_editor(file):
    """باز کردن فایل با ویرایشگر (Vim)"""
    try:
        # بررسی وجود ویرایشگر
        editor = os.getenv('EDITOR', 'vim')
        if not subprocess.run(["which", editor], capture_output=True).returncode == 0:
            editor = 'nano'  # جایگزین اگر vim نصب نباشد
        
        subprocess.run([editor, file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] خطا در باز کردن ویرایشگر: {e}")
    except Exception as e:
        print(f"[!] خطای غیرمنتظره: {e}")

def parse_donut_command(cmd):
    """تبدیل دستورات سفارشی به دستورات سیستمی"""
    for pattern, bash_cmd in donut_lang.items():
        if "{pkg}" in pattern:
            regex = re.escape(pattern).replace(r"\{pkg\}", r"(.+)")
            match = re.match(regex, cmd)
            if match:
                value = match.group(1).strip()
                return bash_cmd.replace("{pkg}", value)
        elif cmd.strip() == pattern:
            return bash_cmd
    return cmd

def execute_system_command(cmd, is_sudo, cwd):
    """اجرای ایمن دستورات سیستمی"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            executable="/bin/bash" if os.path.exists("/bin/bash") else None,
            timeout=60  # محدودیت زمانی اجرا
        )
        
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print(f"[!] {result.stderr.strip()}")
            
    except subprocess.TimeoutExpired:
        print("[!] خطا: زمان اجرای دستور به پایان رسید")
    except Exception as e:
        print(f"[!] خطا در اجرای دستور: {e}")

def run_command(cmd, is_sudo, cwd):
    """مدیریت اصلی دستورات ورودی"""
    cmd = cmd.strip()
    
    # حالت دستورات AI
    if cmd.lower().startswith(("ai:", "ai ")):
        prompt = cmd.split(":", 1)[-1].strip()
        if not prompt:
            print("[!] لطفاً پیام خود را بعد از ai: وارد کنید")
            return
        
        # فقط یک بار پاسخ بدهد
        try:
            response = ask_ai("ollama", prompt)
            if response and isinstance(response, str):
                print(f"[AI 🧠]: {response}")
            return  # خروج بعد از اولین پاسخ
        except Exception as e:
            print(f"[!] خطا در ارتباط با هوش مصنوعی: {e}")
            return

    # حالت دستورات سفارشی
    parsed_cmd = parse_donut_command(cmd)
    if parsed_cmd != cmd:
        execute_system_command(parsed_cmd, is_sudo, cwd)
        return

    # حالت دستورات عادی
    execute_system_command(cmd, is_sudo, cwd)