class Unit:
    def __init__(self):
        self._cost = 0

    def get_cost(self):
        return self._cost


class Engine(Unit):
    def __init__(self, capacity):
        super().__init__()
        if capacity == 1600:
            self._cost = 20000
        elif capacity == 2000:
            self._cost = 25000


class Aircond(Unit):
    def __init__(self, category):
        super().__init__()
        if category == 'auto':
            self._cost = 12000
        elif category == 'manual':
            self._cost = 10000


class Sound(Unit):
    def __init__(self):
        super().__init__()
        self._cost = 2000
