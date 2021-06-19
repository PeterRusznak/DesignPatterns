from duck import Duck


class MallardDuck(Duck):

    def __repr__(self) -> str:
        return "MALLARD"

    def display(self) -> str:
        return f"EZ EGY {self} KACSA"
        


