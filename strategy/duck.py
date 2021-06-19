from __future__ import annotations
from abc import ABC, abstractmethod

class Duck(ABC):

    def __init__(self):
        self._flybehaviour = ''
    
    def performFly(self):
        self._flybehaviour.fly()


    @abstractmethod
    def display(self)-> str:
        pass    

    def quack(self):
        print("QUACK")

    def swim(self):
        print("SWIM")
    