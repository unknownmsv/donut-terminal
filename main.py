from core.shell import DonutShell
from config.install import check_and_install_requirements
from apps.apps import install_app

if __name__ == "__main__":
    check_and_install_requirements()
    shell = DonutShell()
    shell.run()
    