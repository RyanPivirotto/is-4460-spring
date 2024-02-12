class vehicle:
    def __init__(self, make, model, year, color, sound):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.sound = sound
    
    def honk(self):
        return self._sound
    
    def wheels(self):
        return self._wheels

class car(vehicle):
    def __init__(self,make,model,year,color,sound):
        super().__init__(make,model,year,color,sound)
        self.wheels = 4

class motorcycle(vehicle):
    def __init__(self,make,model,year,color,sound):
        super().__init__(make,model,year,color,sound)
        self.wheels = 2