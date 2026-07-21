import subprocess
import sys

def run(script):
    print(f"{script}")
    subprocess.run([sys.executable, script], check=True)

def main():
    run("extract.py")
    run("build_tiles.py"),
    print("обработка успешно завершена")

if __name__ == "__main__":
    main()