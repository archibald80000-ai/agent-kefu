"""Deduplicate sample products for the public learning edition."""

from pathlib import Path


def main():
    source = Path(__file__).resolve().parents[1] / "01_clean" / "clean_products.csv"
    target = Path(__file__).resolve().parents[1] / "01_clean" / "deduplicated_products.csv"
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Deduplicated sample written to {target}")


if __name__ == "__main__":
    main()
