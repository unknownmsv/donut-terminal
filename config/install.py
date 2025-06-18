import shutil
import subprocess

def install_package(pkg):
    print(f"[+] Checking for {pkg}...")
    if shutil.which(pkg) is None:
        print(f"[!] {pkg} not found. Installing...")
        try:
            subprocess.run(["apt", "install", "-y", pkg], check=True)
        except subprocess.CalledProcessError:
            print(f"[!] Failed to install {pkg}")
    else:
        print(f"[✓] {pkg} already installed.")

def check_and_install_requirements():
    packages = [
        "vim",
        "nano",
        "wget",
        "curl",
        "python3",
        "git",
        "pulseaudio"
    ]

    for pkg in packages:
        install_package(pkg)