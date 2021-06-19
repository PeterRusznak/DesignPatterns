from fly.fly_with_wings import FlyWithWings
from duck import AbstractDuck


class MallardDuck(AbstractDuck):

    def __init__(self):
        self._flying_strategy = FlyWithWings()

    def __repr__(self) -> str:
        return "MALLARD KACSA"

    def display(self):
        return print(self)
