#!/usr/bin/env python
class Calculator:
    def __init__(self, var=None):
        if var is None:
            var = 0.0
        self.var = var
        
    def add(self, var1):
        result =  self.var + float(var1)
        self.var = result
        return result

    def sub(self, var1):
        result = self.var - float(var1)
        self.var = result
        return result
    
    def div(self, var1):
        result = self.var / float(var1)
        self.var = result
        return result
    
    def mul(self, var1):
        result = self.var * float(var1)
        self.var = result
        return result
    
    def result(self):
        return self.var
