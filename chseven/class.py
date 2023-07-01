# class Planet:

#     def __init__(self):
#         self.name = 'Hoth'
#         self.radius = 200000
#         self.gravity = 5.5
#         self.system = 'Hoth System'

#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'


# hoth = Planet()
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'The gravity is {hoth.gravity}')
# print(hoth.orbit())

# PlanetX = Planet()

class Nigeria:
    def __init__(self):

        self.name = "Nigeria"
        self.president = "Bola Hammed Tinubu"
        self.state = 36
        self.local_government = 774
        self.continent = 'Afica'

    def country(self):
        return f'{self.name} is presided over by {self.president} a country with {self.state} states and {self.local_government} local governments which is locate in {self.continent} continent'

nation = Nigeria()

print(f'The name of the country is: {nation.name}')
print(f'The name of the newly elected President is: {nation.president}')
print(f'{nation.name} has {nation.local_government} local government and {nation.state} state')
print(f'{nation.name} is located in {nation.continent}')
print(nation.country())




