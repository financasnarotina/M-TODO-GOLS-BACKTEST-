from typing import Literal, List, Dict, Any, Optional
from pydantic import BaseModel, Field

MethodStatus = Literal[
    "Premium Monetizado",
    "Premium Estrutural",
    "Ativo",
    "Ativo Controlado",
    "Seletivo",
    "Sombra Numerica",
    "Bloqueado",
]

class Criterion(BaseModel):
    field: str
    op: Literal[">=", "<=", "==", "between"]
    value: float | int | list[float] | list[int]
    label: str

class MethodDefinition(BaseModel):
    code: str
    name: str
    status: MethodStatus
    evidence_type: Literal["Monetizado", "Estrutural"]
    market: str
    objective: str
    auto_approve: bool = True
    criteria: List[Criterion] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)

class LeagueDefinition(BaseModel):
    league: str
    aliases: List[str] = Field(default_factory=list)
    methods: List[MethodDefinition] = Field(default_factory=list)
    shadow_methods: List[str] = Field(default_factory=list)
    blocked_notes: List[str] = Field(default_factory=list)

class Etapa0(BaseModel):
    banca_inicial: float
    meta_final: float
    n_entradas_max: int
    nome_do_projeto: str
    casa_de_aposta: str
    stake_real_padrao: float

class CriterionResult(BaseModel):
    label: str
    field: str
    op: str
    cutoff: Any
    found: Any
    passed: bool

class MethodEvaluation(BaseModel):
    method_code: str
    method_name: str
    status: str
    evidence_type: str
    market: str
    objective: str
    criteria_results: List[CriterionResult]
    passed: bool
    blocks: List[str] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)
