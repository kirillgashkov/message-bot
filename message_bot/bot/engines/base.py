"""
Abstract bot engine.
"""

from abc import ABC, abstractmethod
from typing import Callable, Optional


class BaseEngine(ABC):

    @abstractmethod
    def message(self, recipient_id: str, m: str):
        pass

    @abstractmethod
    def error(self, recipient_id: str, m: str, e: Optional[Exception]):
        pass

    @abstractmethod
    def run(self, message_handler: Callable[[str, str], None]):
        pass
