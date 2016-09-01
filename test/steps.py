#! /bin/env python
import unittest
import sys
import os
sys.path.append(os.path.join('../gutenBorg/steps'))
import json
import subprocess as sp
from filecmp import cmp as compare_file

from pandoc import pandoc as pandoc
from Markdown import Markdown as Markdown
from knitr import knitr as knitr
from shell import shell as shell


def loadconfig(filename):
    with open(filename) as f:
        d=json.load(f)
    return(d)

def compare(fileA,fileB):
    compare_file(fileA,fileB,shallow=False) 
    return(True)

class steps_test(unittest.TestCase):
    def setUp(self):
        sp.call('rm ./output/* &> /dev/null',shell=True)      
    
    def test_pandoc(self):
        config=loadconfig('./input/pandoc.json')
        pandoc(**config)
        
        self.assertTrue(
            compare(config['input'],config['output']) 
        )

    def test_shell(self):
        config=loadconfig('./input/shell.json')
        shell(**config)
        
        self.assertTrue(
            compare(config['input'],config['output']) 
        )

    def test_knitr(self):
        config=loadconfig('./input/knitr.json')
        knitr(**config)
        
        self.assertTrue(
            compare(config['input'],config['output']) 
        )

    def test_markdown(self):
        config=loadconfig('./input/markdown.json')
        Markdown(**config)
        
        self.assertTrue(
            compare(config['input'],config['output']) 
        )

if __name__ == '__main__':
    unittest.main()



