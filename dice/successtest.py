'''Roll dice in a success-test style manner, returning
the number of "hits" and (optionally) "misses" for a given
roll.'''
from dice.dice import Dice
import math

class SuccessTest(Dice):
    "Success-test style rolling for ShadowRun (six-sided with hits and misses"

    def __init__(self, pool=5, threshold=2, edge_test=False):
        '''Set initial values for rolls, sides, add
        and success test-specific values for threshold'''
        super().__init__(1,6,0)

        #for Edge rolls
        self.edge = edge_test

        self.setDice(1,6,0)

        self.pool = pool
        self.threshold = threshold
        self.results_pool = []

        #threshold constants
        self.EASY = 1
        self.AVERAGE = 2
        self.HARD = 4
        self.VERY_HARD = 6
        self.EXTREME8 = 8
        self.EXTREME9 = 9
        self.EXTREME10 = 10

    @property
    def pool(self):
        return self._pool

    @pool.setter
    def pool(self, pool):
        '''Sets pool and computes glitch threshold while doing so'''
        self._pool = pool
        self.glitch_threshold = int(math.ceil((self.pool/2)))

    def clear(self):
        '''set up and return empty results array'''
        self.result = ''
        self.critical_glitch = False
        self.results = []

    def setupTest(self, pool, threshold, edge_test=False):
        '''setup new test'''
        self.pool = pool
        self.threshold = threshold
        self.edge = edge_test

    def setEdgeTest(self, edge_test):
        '''Turn on or off flag to indicate this is an Edge test'''
        self.edge = edge_test

    def rollSingleTest(self):
        """single dice component of test

        returns typle:
        (result INT, hit/miss STR)"""
        DIFFICULTY = 4
        result = self.roll()
        outcome = ''
        if result > DIFFICULTY:
            #a hit
            outcome = 'hit'
        elif result ==1:
            outcome = 'glitch'
        else:
            outcome = 'miss'
        return(result,outcome)

    def rollTest(self):
        """Roll the number of dice in a pool, and return a tuple consisting
        of the final result (True = hit, False=miss), a crtitical glitch flag,
        and a results array

        returns tuple:
            (result BOOL,
            glitch BOOL,
            critical_glitch BOOL,
            results SORTED INT LIST)"""
        self.clear()
        self.results_pool = []
        self.outcome = {'hit': 0,'glitch': 0,'miss': 0}
        self.glitch = False
        self.critical_glitch = False

        for roll in range(self.pool):
            result, result_txt = self.rollSingleTest()
            self.results_pool.append(result)
            self.outcome[result_txt] += 1
            #rule of six for edge test
            if (self.edge) & (result == 6):
                ros_result = result
                while(ros_result == 6):
                    ros_result, ros_text = self.rollSingleTest()
                    self.results_pool.append(ros_result)
                    self.outcome[ros_text] += 1

        #check for glitch
        if self.outcome['glitch'] >= self.glitch_threshold:
            self.glitch = True

        #check for success
        if self.outcome['hit'] >= self.threshold:
            self.result = True
        else:
            self.result = False
            if self.glitch:
                self.critical_glitch = True

        #results should be accesssable as class property
        self.results = self.results_pool

        return self.result, self.glitch, self.critical_glitch, sorted(self.results)

