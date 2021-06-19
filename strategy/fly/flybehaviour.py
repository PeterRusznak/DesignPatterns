from __future__ import annotations
from abc import ABC, abstractmethod

class FlyBehaviour(ABC):

    @abstractmethod
    def fly(self):
        pass
