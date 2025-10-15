import sys

HELP_TEXT = """Використання:
  python src/sys_tool.py [--help]

Опис:
  Скрипт друкує "командна строка" лише при прямому запуску.
  При імпорті як модуль нічого не друкує.
"""

def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] in ("--help", "-h"):
        print(HELP_TEXT)
        return 0
    print("командна строка")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
