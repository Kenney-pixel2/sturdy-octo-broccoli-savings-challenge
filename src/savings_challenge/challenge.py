from dataclasses import dataclass, field


@dataclass
class Challenge:
    name: str
    target_amount: int
    target_days: int
    completed_days: int = field(default=0)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Challenge name cannot be empty.")

        if self.target_amount <= 0:
            raise ValueError("Target amount must be greater than zero.")

        if self.target_days <= 0:
            raise ValueError("Target days must be greater than zero.")

    def amount_for_day(self, day: int) -> int:
        return self.target_amount // self.target_days
