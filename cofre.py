from datetime import datetime
from app.database import get_connection


def upsert_cofre_geral(payload: dict) -> None:
    conn = get_connection()
    payload = payload.copy()
    payload.setdefault("ultima_atualizacao", datetime.now().isoformat(timespec="seconds"))
    columns = ", ".join(payload.keys())
    placeholders = ", ".join(["?"] * len(payload))
    conn.execute(f"INSERT INTO cofre_geral ({columns}) VALUES ({placeholders})", list(payload.values()))
    conn.commit()
    conn.close()
