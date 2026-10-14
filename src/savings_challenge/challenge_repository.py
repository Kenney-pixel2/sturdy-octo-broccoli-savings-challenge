import json
from pathlib import Path

from savings_challenge.challenge import Challenge


class ChallengeRepository:
    def save(self, challenges: list[Challenge], file_path: Path) -> None:
        data = [challenge.to_dict() for challenge in challenges]
        file_path.write_text(json.dumps(data), encoding="utf-8")

    def load(self, file_path: Path) -> list[Challenge]:
        if not file_path.exists():
            return []

        data = json.loads(file_path.read_text(encoding="utf-8"))
        return [Challenge.from_dict(item) for item in data]
