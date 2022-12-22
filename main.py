class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    
  def func(self):
    print(f'I am going to buy {self.brand} {self.model}')

c1 = Car('bmw', 'x6')
c1.func()