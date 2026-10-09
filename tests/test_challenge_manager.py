from savings_challenge.challenge import Challenge
from savings_challenge.challenge_manager import ChallengeManager


def test_add_challenge_appears_in_challenges() -> None:
    manager = ChallengeManager()
    challenge = Challenge(name="Vacation", target_amount=300, target_days=3)

    manager.add_challenge(challenge)

    assert manager.challenges == (challenge,)


def test_find_challenge_returns_matching_challenge() -> None:
    manager = ChallengeManager()
    challenge = Challenge(name="Vacation", target_amount=300, target_days=3)
    manager.add_challenge(challenge)

    found = manager.find_challenge("Vacation")

    assert found is challenge


def test_find_challenge_returns_none_when_not_found() -> None:
    manager = ChallengeManager()

    found = manager.find_challenge("Vacation")

    assert found is None


def test_remove_challenge_removes_it_from_challenges() -> None:
    manager = ChallengeManager()
    challenge = Challenge(name="Vacation", target_amount=300, target_days=3)
    manager.add_challenge(challenge)

    manager.remove_challenge(challenge)

    assert manager.challenges == ()
