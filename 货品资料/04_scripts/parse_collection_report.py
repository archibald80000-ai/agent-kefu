"""Parse a collection report template for the public learning edition."""

from pathlib import Path


def main():
    report = Path(__file__).resolve().parents[1] / "00_总表" / "商品采集报告_示例.md"
    print(report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
