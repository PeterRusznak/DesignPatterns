from flyable import Flyable
from duck import Duck


class RedHead(Duck, Flyable):


    def __repr__(self) -> str:
        return "REDHEAD"

    def display(self) -> str:
        return f"EZ EGY {self} KACSA"
       