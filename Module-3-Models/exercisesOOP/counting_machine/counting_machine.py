class CountingMachine:
    def __init__(self) -> None:
        self.count = 0
    def inc(self):
        self.count += 1
    def dec(self):
        self.count -= 1