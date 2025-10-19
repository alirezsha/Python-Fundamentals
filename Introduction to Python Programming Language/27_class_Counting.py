class Counting:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.value = v
        self.incr = i
        
    def __repr__(self) -> str:
        return str(self.value)
    
    def increase(self) -> None:
        self.value += self.incr
