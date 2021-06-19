from __future__ import annotations
from abc import ABC, abstractmethod

class Duck(ABC):
    
    @abstractmethod
    def display(self)-> str:
        pass    

    def quack(self):
        print("QUACK")

    def swim(self):
        print("SWIM")
    