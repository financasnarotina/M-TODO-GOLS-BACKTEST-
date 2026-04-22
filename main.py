from fastapi import FastAPI
from pydantic import BaseModel
from app.database import init_db
from app.engine.method_loader import find_league_by_name
from app.engine.evaluator import evaluate_method
from app.engine.response_builder import build_pre_game_response
from app.engine.models import Etapa0

app = FastAPI(title="Projeto Bot Gols")

class AnalyzePayload(BaseModel):
    etapa0: Etapa0
    league: str
    features: dict
    banca_atual: float | None = None
    entrada_atual: int = 1


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.post("/analyze")
def analyze(payload: AnalyzePayload) -> dict:
    league = find_league_by_name(payload.league)
    if not league:
        return {"error": f"Liga nao oficial ou nao encontrada: {payload.league}"}
    evaluations = [evaluate_method(method, payload.features) for method in league.methods]
    response_text = build_pre_game_response(
        etapa0=payload.etapa0,
        banca_atual=payload.banca_atual or payload.etapa0.banca_inicial,
        entrada_atual=payload.entrada_atual,
        avaliacoes=evaluations,
    )
    return {
        "league": league.league,
        "methods_tested": len(evaluations),
        "response_text": response_text,
    }
