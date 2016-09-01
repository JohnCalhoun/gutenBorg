import unittest
import sys
import os
sys.path.append(os.path.join('..'))
from gutenBorg import pipeline

class pipeline_test(unittest.TestCase):
    def test_load(self):
        pl=pipeline(filename='./input/recipe.json') 

    def test_render(self):
        pl=pipeline(filename='./input/recipe.json') 
        pl.start()
        pl.join()

if __name__ == '__main__':
    unittest.main()
