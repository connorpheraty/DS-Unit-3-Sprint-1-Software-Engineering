import unittest
import random

# Create Parent class
class Product:

    def __init__(self, name = None, price = 10, weight=20, integer=20,
                 flammability=0.5, identifier = random.randint(1000000, 9999999)):
        self.name = name 
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    # Method that determines the stealability of a product
    def stealability(self):

        steal_factor = self.price / self.weight

        if steal_factor < .5:
            return('Not so stealable...')

        elif steal_factor >= .5 and steal_factor < 1:
            return('Kinda stealable')
        
        else:
            return('Very stealable')

    # Method that determines the explosiveness of a product
    def explode(self):

        explode_factor = self.flammability * self.weight

        if explode_factor < 10:
            return('...fizzle')

        elif explode_factor >= 10 and explode_factor < 50:
            return('...boom!')

        else:
            return('...BABOOM!')

# BoxingGlove subclass
class BoxingGlove(Product):

    def __init__(self, name = None, price = 10, weight=10, integer=20,
                 flammability=0.5, identifier = random.randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight,integer=integer,
                         flammability=flammability, identifier=identifier)

    # Method to determine the 'punch factor'    
    def punch(self):
        if self.weight < 5:
            return("That tickles")
        elif self.weight >=5 and self.weight <15:
            return('Hey that hurt!')
        else:
            return('OUCH!')

    # Method overriding parent method for the BoxingGlove class
    def explode(self):
        return("...it's a glove.")
