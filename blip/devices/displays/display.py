class Display:
    width: int
    height: int

    def clear(self, color: int):
        raise NotImplementedError

    def text(self, string: str, x: int, y: int, color: int):
        raise NotImplementedError

    def show(self):
        raise NotImplementedError
