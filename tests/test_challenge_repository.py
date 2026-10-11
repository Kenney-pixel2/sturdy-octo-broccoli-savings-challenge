from pathlib import Path

from savings_challenge.challenge import Challenge
from savings_challenge.challenge_repository import ChallengeRepository


def test_save_then_load_round_trips_challenges(tmp_path: Path) -> None:
    repository = ChallengeRepository()
    file_path = tmp_path / "challenges.json"
    challenges = [
        Challenge(name="Vacation", target_amount=300, target_days=3, completed_days=1),
        Challenge(name="Laptop", target_amount=1000, target_days=10),
    ]

    repository.save(challenges, file_path)

    assert repository.load(file_path) == challenges
