"""Build a formal catalog sample for the public learning edition."""

from pathlib import Path


def main():
    target = Path(__file__).resolve().parents[1] / "02_catalog" / "正式商品目录总表.csv"
    target.write_text(
        "catalog_id,normalized_name,display_name,version_tier,duration,suggested_price\n"
        "CAT-001,示例服务标准版,示例服务标准版,标准版,12个月,199\n",
        encoding="utf-8",
    )
    print(f"Catalog sample written to {target}")


if __name__ == "__main__":
    main()
