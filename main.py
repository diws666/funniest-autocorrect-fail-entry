import os

ENTRY_LINE = (
    "I meant to text meeting at noon but autocorrect sent meeting at the moon. "
    "I am now the only one in the office with a spacesuit."
)


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_LINE)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
