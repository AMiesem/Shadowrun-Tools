import unittest
from dice import dice
from dice import successtest

class DiceTests(unittest.TestCase):

    # setup and teardown functions
    def setUp(self):
        self.d=dice.Dice()
    def tearDown(self):
        del self.d

    # test rolling dice
    def test_base_dice_roll(self):
        '''roll dice of different sides and numbers, making sure they stay within
        acceptable parameters'''
        geometry = [4,6,8,10,12,20,30,100]
        for sides in geometry:
            for rolls in range(100):
                self.d.setSides(sides)
                result = self.d.roll()
                self.assertGreater(result,0,msg='Result less than one (r: {} s: {} #: {})'.format(result,sides,rolls))
                self.assertLessEqual(result,sides,
                                     msg='greater than sides (r: {} s: {} #: {})'.format(result,sides,rolls))


if __name__ == '__main__':
    unittest.main()
