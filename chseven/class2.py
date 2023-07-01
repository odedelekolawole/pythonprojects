class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} has a gravity of {self.gravity}'


Hoth = Planet('Hoth', 200000, 5.5, "Hoth System")
print(f'The name is: {Hoth.name}')
print(f'The radius is: {Hoth.radius}')
print(f'The gravity is: {Hoth.gravity}')
print(f'The system is: {Hoth.system}')
print(Hoth.orbit())

Nebula = Planet('Nebula', 350000, 2.9, 'Nebula Syytem')
print(f'The name is: {Nebula.name}')
print(f'The radius is: {Nebula.radius}')
print(f'The gravity is: {Nebula.gravity}')
print(f'The system is: {Nebula.system}')
print(Nebula.orbit())
