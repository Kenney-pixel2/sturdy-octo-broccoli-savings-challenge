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
