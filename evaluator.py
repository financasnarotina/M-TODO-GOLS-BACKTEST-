from typing import Any, Dict
from app.engine.models import MethodDefinition, CriterionResult, MethodEvaluation


def _check(op: str, found: Any, cutoff: Any) -> bool:
    if found is None:
        return False
    if op == ">=":
        return found >= cutoff
    if op == "<=":
        return found <= cutoff
    if op == "==":
        return found == cutoff
    if op == "between":
        low, high = cutoff
        return low <= found <= high
    raise ValueError(f"Operador nao suportado: {op}")


def evaluate_method(method: MethodDefinition, features: Dict[str, Any]) -> MethodEvaluation:
    results = []
    blocks = []
    method_pass = True
    for c in method.criteria:
        found = features.get(c.field)
        passed = _check(c.op, found, c.value)
        if not passed:
            method_pass = False
        results.append(CriterionResult(
            label=c.label,
            field=c.field,
            op=c.op,
            cutoff=c.value,
            found=found,
            passed=passed,
        ))
    if method.status in {"Sombra Numerica", "Bloqueado"}:
        blocks.append(f"Metodo com status {method.status}")
        method_pass = False
    return MethodEvaluation(
        method_code=method.code,
        method_name=method.name,
        status=method.status,
        evidence_type=method.evidence_type,
        market=method.market,
        objective=method.objective,
        criteria_results=results,
        passed=method_pass,
        blocks=blocks,
        notes=method.notes,
    )
