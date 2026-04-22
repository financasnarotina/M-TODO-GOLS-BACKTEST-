from typing import Any, Dict

class CollectorResult(dict):
    """Container simples para devolver dados normalizados e origem."""


class BaseCollector:
    name = "base"

    def fetch(self, league: str, home_team: str, away_team: str) -> Dict[str, Any]:
        raise NotImplementedError
