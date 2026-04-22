import json
from pathlib import Path
from app.config import settings


def build_catalog() -> dict:
    data_dir = Path(settings.data_dir)
    files = sorted([p.name for p in data_dir.glob('*.csv')])
    return {"csv_files": files, "count": len(files)}


def save_catalog(output_path: str) -> None:
    catalog = build_catalog()
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
