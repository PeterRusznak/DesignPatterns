

from fly.fly_no_way import FlyNoWay
from duck import AbstractDuck


class GumiKacsa(AbstractDuck):

    def __init__(self):
        self._flying_strategy = FlyNoWay()

    def __repr__(self) -> str:
        return "GUMI KACSA"

    def display(self):
        return print(self)