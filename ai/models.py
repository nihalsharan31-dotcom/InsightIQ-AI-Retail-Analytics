from dataclasses import dataclass


@dataclass
class AIResponse:
    answer: str
    confidence: float = 0.0