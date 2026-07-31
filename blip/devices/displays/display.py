class Display:
    width: int
    height: int

    def clear(self, color: int):
        raise NotImplementedError

    def show(self):
        raise NotImplementedError
