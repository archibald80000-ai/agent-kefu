"""Build a sample product knowledge file for the public learning edition."""

from pathlib import Path
import json


def main():
    target = Path(__file__).resolve().parents[1] / "03_knowledge_base" / "products" / "DEMO-001.json"
    data = {
        "product_id": "DEMO-001",
        "normalized_name": "示例服务标准版",
        "delivery_method": "系统交付",
        "risk_note": "仅用于学习结构",
    }
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Product KB sample written to {target}")


if __name__ == "__main__":
    main()
