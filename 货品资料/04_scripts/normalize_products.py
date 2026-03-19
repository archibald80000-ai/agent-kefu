"""Normalize sample products for the public learning edition."""

from pathlib import Path


def main():
    target = Path(__file__).resolve().parents[1] / "01_clean" / "clean_products.csv"
    print(f"Use {target} as the normalized sample dataset.")


if __name__ == "__main__":
    main()
