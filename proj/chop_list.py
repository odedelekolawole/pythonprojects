# class Tab:

#     menu = {
#         'wine': 5,
#         'beer': 3,
#         'soft_drink': 2,
#         'chicken': 10,
#         'beef': 15,
#         'veggie': 12,
#         'dessert': 6
#     }

#     def __init__(self):
#         self.total = 0
#         self.items = []

#     def add(self, item):
#         self.items.append(item)
#         self.total += self.menu[item]

#     def print_bill(self, tax, service):
#         tax = (tax/100) * self.total
#         service = (service/100) * self.total
#         total = self.total + tax + service

#         for item in self.items:
#             print(f'{item:20} £{self.menu[item]}')

#         print(f'{"Total":20} £{total:.2f}')


class Shop:

    groceries = {
        'yoghurt': 2500,
        'soap': 1000,
        'nut': 1200,
        'coffee': 750,  
        'tea': 800,
        'biscuit': 500,
        'chocolate': 1650,
        'bread': 700,
        'brush': 200
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def count(self, item):
        self.items.append(item)
        self.total += self.groceries[item]

    def item_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

    for item in self.items:
        print(f'{item:40} £{self.groceries[item]}')

        print(f'{"Total":40}  {total:.2f}')
    

