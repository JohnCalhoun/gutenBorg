from threading import Thread
import json

import steps as Steps
from steps import *


class pipeline(Thread):
    """Document rendering pipeline, reads in config or dict and runs in another thread""" 
    
    def __init__(self,variables=None,filename=None):
        """creates pipeline from file using filename or dict using variables""" 
        super(pipeline,self).__init__() 
                
        if filename:
            self.load_recipe_from_file(filename)
        elif variables:
            self.load_recipe_from_dict(filename)

    def load_recipe_from_file(self,filename):
        with open(filename) as f:
            variables=json.load(f)
        self.load_recipe_from_dict(variables)  
    
    def load_recipe_from_dict(self,dictionary):
        self.logfile=dictionary['logfile']
        self.errorfile=dictionary['errorfile']
        self.steps=dictionary['steps'] 

    def run(self):
        for step  in self.steps:
            name=step['name']
            func=vars(getattr(Steps,name))[name]
            func(**step['opts'])




