#import re
#from collections import deque

from .qrandom import QuantumRandomInt
from .bank import CHARACTER, SITUATION

class PromptGenerator:
    def __init__(self):
        self.character_chooser = QuantumRandomInt(0, len(CHARACTER) - 1)
        self.situation_chooser = QuantumRandomInt(0, len(SITUATION) - 1)
        
    
    def generate_preposition(self, letter):
        if letter.lower() in 'aeiou':
            prep = "An "
        else:
            prep = "A "
        
        return prep
        
    def generate_prompt(self,**kwargs):
            idxc = self.character_chooser.generate(1, **kwargs)[0]
            idxs = self.situation_chooser.generate(1, **kwargs)[0]
            char = CHARACTER[idxc]
            second = SITUATION[idxs]
            prep = self.generate_preposition(char[0])

            prompt = prep + char.lower() + " " + " who " + second.lower() + "."
            return prompt