

from fly.flybehaviour import AbstractFlyStrategy


class FlyNoWay(AbstractFlyStrategy):

    def fly(self):
        print("NEM repül, nem tud")
