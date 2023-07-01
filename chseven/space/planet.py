class Planet:

    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} has a gravity of {self.gravity}'

    @classmethod
    def common(cls):
        return f'All planets are {cls.shape} in shape because of gravity'

    @staticmethod
    def spin(speed = '2000 mile per hour'):
        return f'The planet spin and spina at {speed}'
