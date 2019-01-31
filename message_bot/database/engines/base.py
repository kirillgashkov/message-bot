"""
Abstract database engine.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class BaseEngine(ABC):

    def __init__(self):
        self.table = dict()

    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pull(self):
        pass

    def write(self, key: str, fields: Dict[str, str]):
        self.table[key] = fields

    def read(self, key: str) -> Optional[Dict[str, str]]:
        return self.table.get(key)

    def read_all(self) -> Dict[str, Dict[str, str]]:
        return self.table

    def update(self, key: str, fields: Dict[str, str]):
        if key not in self.table:
            self.table = dict()
        self.table[key].update(fields)

    def delete(self, key: str):
        del self.table[key]
