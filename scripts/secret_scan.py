from pathlib import Path
import re
import sys

PATTERN = re.compile(
    r"""(?i)\b(api_key|secret|token|password)\b\s*[:=]\s*["'][^"']{8,}["']"""
)

SKIP = {
    ".git",
    ".venv",
    ".venv-1",
    "venv",
    "__pycache__",
    ".pytest_cache"
}

def main():
    failed = False
    scanner_file = Path(__file__).resolve()

    for path in Path(".").rglob("*"):
        if not path.is_file() or any(part in SKIP for part in path.parts):
            continue

        if path.resolve() == scanner_file:
            continue

        if path.name == ".env":
            print(f"Potential secret file: {path}")
            failed = True
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        for number, line in enumerate(content.splitlines(), 1):
            if PATTERN.search(line) or "-----BEGIN PRIVATE KEY-----" in line:
                print(f"Potential secret pattern: {path}:{number}")
                failed = True

    print("Secret scan failed." if failed else "Secret scan passed.")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
