from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractDuck(ABC):

    def __init__(self):
        self._flying_strategy = None

    @abstractmethod
    def display(self):
        pass

    def swim(self):
        print("ÚSZOK")

    def perform_fly(self):
        self._flying_strategy.fly()    