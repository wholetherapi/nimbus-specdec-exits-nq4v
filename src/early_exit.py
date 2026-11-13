"""Early-exit transformer patch used by the WMT workshop paper."""
from __future__ import annotations


class EarlyExitHead:
    def __init__(self, hidden_size: int, vocab_size: int):
        self.weight = [[0.0] * hidden_size for _ in range(vocab_size)]

    def logits(self, hidden: list[float]) -> list[float]:
        return [sum(a * b for a, b in zip(row, hidden)) for row in self.weight]
