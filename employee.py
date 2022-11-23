from experta import*
from random import randint

class rating(Fact):
    """info of rating"""
    pass
class ees(KnowledgeEngine):
    
    @Rule(rating(L(5)))
    def nice(self):
        print("Awesome Employee")
    
    @Rule(rating(L(4)))
    def good(self):
        print("good Employee")
    
    @Rule(rating(L(3)))
    def average(self):
        print("average Employee")
        
    @Rule(rating(L(2)))
    def bavg(self):
        print("needs improvement")
        
    @Rule(rating(L(1)))
    def low(self):
        print("poor performance of Employee")
engine = ees()
engine.reset()
engine.declare(rating(randint(1,5)))
engine.run()