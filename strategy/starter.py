from flyable import Flyable
from gumi_duck import GumiDuck
from redhead_duck import RedHead
from mallard_duck import MallardDuck

m = MallardDuck()
r = RedHead()
g = GumiDuck()

kacsak = [m, r, g]
for k in kacsak:
    if isinstance(k, Flyable):
        k.fly()
    else:
        print(k.display())
        




