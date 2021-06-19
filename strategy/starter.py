
from gumi_duck import GumiKacsa
from mallard_duck import MallardDuck

m = MallardDuck()
g = GumiKacsa()

kacsak = [m,g]

for k in kacsak:
    k.display()
    k.swim()
    k.perform_fly()
