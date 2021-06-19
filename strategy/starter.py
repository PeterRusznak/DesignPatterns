from gumi_duck import GumiDuck
from mallard_duck import MallardDuck

m = MallardDuck()
g = GumiDuck()

kacsak = [m, g]
for k in kacsak:
    print(k.display())    
    k.performFly()

    
        




