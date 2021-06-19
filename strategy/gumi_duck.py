
from fly.flynoways import FlyNoWay
from duck import Duck

class GumiDuck(Duck):

    def __init__(self):
        super().__init__()
        self._flybehaviour = FlyNoWay()

    def __repr__(self) -> str:
        return "GUMI"

    def display(self) -> str:
        return f"EZ EGY {self} KACSA"
        
   
