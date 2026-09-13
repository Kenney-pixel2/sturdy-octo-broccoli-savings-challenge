from savings_challenge.challenge import Challenge


def test_new_challenge_starts_with_no_completed_days() -> None:
    challenge = Challenge(name="Vacation", target_amount=1000, target_days=30)

    assert challenge.name == "Vacation"
    assert challenge.target_amount == 1000
    assert challenge.target_days == 30
    assert challenge.completed_days == 0
