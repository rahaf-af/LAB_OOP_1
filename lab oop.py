class Panda:
    def __init__(self, name, age, color, weight):
         self.name = name      
         self.age = age        
         self.color = color    
         self.weight = weight  
    def eat(self, food):
        print(f"{self.name} is eating {food}.")
    def sleep(self):
        print(f"{self.name} is sleeping.")