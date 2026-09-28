from collections import OrderedDict
from typing import Any, Tuple


class LRUInferenceCache:
    def __init__(self, capacity: int = 128):
        self.capacity = capacity
        self.cache: OrderedDict[Tuple[float, ...], Any] = OrderedDict()
        self.hits = 0
        self.misses = 0

    def get(self, features: Tuple[float, ...]) -> Any | None:
        if features not in self.cache:
            self.misses += 1
            return None
        self.hits += 1
        self.cache.move_to_end(features)
        return self.cache[features]

    def put(self, features: Tuple[float, ...], result: Any) -> None:
        if features in self.cache:
            self.cache.move_to_end(features)
        self.cache[features] = result
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Evicts least recently used item

    def stats(self) -> dict:
        total = self.hits + self.misses
        hit_ratio = (self.hits / total) if total > 0 else 0.0
        return {
            "capacity": self.capacity,
            "size": len(self.cache),
            "hits": self.hits,
            "misses": self.misses,
            "hit_ratio": round(hit_ratio, 3),
        }