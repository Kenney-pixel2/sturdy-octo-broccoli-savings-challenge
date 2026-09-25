import pytest

from savings_challenge.challenge import Challenge


def test_new_challenge_starts_with_no_completed_days() -> None:
    challenge = Challenge(name="Vacation", target_amount=1000, target_days=30)

    assert challenge.name == "Vacation"
    assert challenge.target_amount == 1000
    assert challenge.target_days == 30
    assert challenge.completed_days == 0


def test_challenge_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="name"):
        Challenge(name="", target_amount=1000, target_days=30)


def test_challenge_rejects_non_positive_target_amount() -> None:
    with pytest.raises(ValueError, match="amount"):
        Challenge(name="Vacation", target_amount=0, target_days=30)


def test_challenge_rejects_non_positive_target_days() -> None:
    with pytest.raises(ValueError, match="days"):
        Challenge(name="Vacation", target_amount=1000, target_days=0)


def test_amount_for_day_splits_evenly_when_divisible() -> None:
    challenge = Challenge(name="Vacation", target_amount=300, target_days=3)

    assert challenge.amount_for_day(1) == 100
    assert challenge.amount_for_day(2) == 100
    assert challenge.amount_for_day(3) == 100


def test_amount_for_day_distributes_remainder_to_earliest_days() -> None:
    challenge = Challenge(name="Vacation", target_amount=100, target_days=3)

    assert challenge.amount_for_day(1) == 34
    assert challenge.amount_for_day(2) == 33
    assert challenge.amount_for_day(3) == 33


def test_complete_day_increments_completed_days() -> None:
    challenge = Challenge(name="Vacation", target_amount=300, target_days=3)

    challenge.complete_day()

    assert challenge.completed_days == 1
