"""
Abstract database engine.
"""

import abc
from typing import Dict, Optional, Callable, Mapping

from message_bot.database import _utils


class BaseEngine(abc.ABC):

    def __init__(self):
        self._table = dict()

    @abc.abstractmethod
    def push(self, callback: Callable[[], None] = lambda: ...):
        pass

    @abc.abstractmethod
    def pull(self, callback: Callable[[], None] = lambda: ...):
        pass

    def write(self, key: str, fields: Dict[str, str]):
        self._table[key] = fields

    def read(self, key: str) -> Optional[Mapping[str, str]]:
        if key not in self._table:
            return None
        return _utils.DatabaseView(self._table[key])

    def read_all(self) -> Mapping[str, Mapping[str, str]]:
        return _utils.DatabaseView(self._table)

    def update(self, key: str, fields: Dict[str, str]) -> bool:
        if key not in self._table:
            return False
        self._table[key].update(fields)
        return True

    def delete(self, key: str):
        del self._table[key]
