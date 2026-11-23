"""Write one joke about working beside an AI coding agent to /output/entry.txt."""

from pathlib import Path

JOKE = "My coding agent presented my demo so confidently, the client asked when I started interning for it."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # One fixed string, written exactly as-is, so every run is identical.
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
