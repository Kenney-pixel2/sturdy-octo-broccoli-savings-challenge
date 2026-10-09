from savings_challenge.challenge import Challenge


class ChallengeManager:
    def __init__(self) -> None:
        self._challenges: list[Challenge] = []

    def add_challenge(self, challenge: Challenge) -> None:
        self._challenges.append(challenge)

    @property
    def challenges(self) -> tuple[Challenge, ...]:
        return tuple(self._challenges)

    def find_challenge(self, name: str) -> Challenge | None:
        for challenge in self._challenges:
            if challenge.name == name:
                return challenge

        return None

    def remove_challenge(self, challenge: Challenge) -> None:
        self._challenges.remove(challenge)
