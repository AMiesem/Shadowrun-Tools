'''The Dice object'''

# -*- coding: utf-8 -*-

import random



class Dice:
    '''Object that allows for the creation of single or multiple dice and provides the methods for
    rolling and otherwise manipulatig them.'''

    def __init__(self, rolls=1, sides=6, add=0):
        '''Set initial value for rolls, sides, add'''
        self.rolls = rolls
        self.sides = sides
        self.add = add

    def setDice(self, rolls, sides, add):
        '''Change all three values for object'''
        self.rolls = rolls
        self.sides = sides
        self.add = add

    def setRolls(self, rolls):
        '''Change value for number of rolls'''
        self.rolls = rolls

    def setSides(self, sides):
        '''Change value for number of sides'''
        self.sides = sides

    def setAdd(self, add):
        '''Change value for number to add to roll'''
        self.add = add

    def roll(self):
        '''Perform the dice roll using prescribed values'''
        result = 0
        for rollSeq in range(self.rolls):
            result += random.randint(1, self.sides)

        result += self.add
        return result

