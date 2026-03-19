"""Build FAQ seed data for the public learning edition."""

from pathlib import Path
import json


def main():
    target = Path(__file__).resolve().parents[1] / "03_knowledge_base" / "faq" / "faq_seed.sample.json"
    data = [
        {"scene": "商品简介", "question": "这是什么服务？"},
        {"scene": "使用准备", "question": "需要准备什么？"},
    ]
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"FAQ seed written to {target}")


if __name__ == "__main__":
    main()
