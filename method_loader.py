import json
from pathlib import Path
from app.config import settings
from app.engine.models import LeagueDefinition


def list_method_files() -> list[Path]:
    return sorted(Path(settings.methods_dir).glob('*.json'))


def load_all_leagues() -> list[LeagueDefinition]:
    leagues = []
    for file in list_method_files():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        leagues.append(LeagueDefinition.model_validate(data))
    return leagues


def find_league_by_name(name: str) -> LeagueDefinition | None:
    name_low = name.strip().lower()
    for league in load_all_leagues():
        all_names = [league.league, *league.aliases]
        if any(name_low == n.lower() for n in all_names):
            return league
    return None
