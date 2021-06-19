from flyable import Flyable
from duck import Duck


class MallardDuck(Duck, Flyable):

    def __repr__(self) -> str:
        return "MALLARD"

    def display(self) -> str:
        return f"EZ EGY {self} KACSA"
        


