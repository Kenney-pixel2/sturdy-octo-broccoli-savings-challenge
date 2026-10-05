from savings_challenge.challenge import Challenge
from savings_challenge.challenge_manager import ChallengeManager


def test_add_challenge_appears_in_challenges() -> None:
    manager = ChallengeManager()
    challenge = Challenge(name="Vacation", target_amount=300, target_days=3)

    manager.add_challenge(challenge)

    assert manager.challenges == (challenge,)
