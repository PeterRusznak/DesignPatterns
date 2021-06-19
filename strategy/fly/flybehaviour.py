from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFlyStrategy(ABC):

    @abstractmethod
    def fly(self):
        pass


