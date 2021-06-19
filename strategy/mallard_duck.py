from fly.flywithwings import FlyWithWings
from duck import Duck


class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self._flybehaviour = FlyWithWings() 

    def __repr__(self) -> str:
        return "MALLARD"

    def display(self) -> str:
        return f"EZ EGY {self} KACSA"
        


