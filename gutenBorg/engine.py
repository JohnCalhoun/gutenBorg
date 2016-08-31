from threading import Thread
import json
from steps import *

class engine(Thread):
    def init(self,variables=None,filename=None):
        #if filename then load from file
        #if dict then load from dict
        pass

    def load_recipe_from_file(self,filename):
        #open json file,run load form dict
        pass
    
    def load_recipe_from_dict(self,dictionary):
        #extract out variables 
        #pull out step array 
        pass

    def run(self):
        #loop through step array calling 
        pass
