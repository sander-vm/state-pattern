from __future__ import annotations
from abc import ABC, abstractmethod

class State(ABC):
    @property
    def context(self) -> self:
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

    @abstractmethod
    def handle3(self) -> None:
        pass
