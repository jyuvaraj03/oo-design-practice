from dataclasses import dataclass

@dataclass(frozen=True)
class Outcome:
    name: str
    odds: int

    def winAmount(self, amount: float) -> float:
        """
        Multiply this Outcome's odds by the given amount. The product is returned.
        :params amount(float): amount being bet 
        """
        return self.odds * amount

    def __str__(self) -> str:
        return f'{self.name} ({self.odds}:1)'
