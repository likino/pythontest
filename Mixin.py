class Animal(object):
	pass
	
class Mammal(Animal):
	pass

class RunnableMixin(object):
	def run(self):
		print ('Running...')
		
class FlyableMixin(object):
	def fly(self):
		print('Flying...')
		
class CarnivorousMixin(object):
	def Car(self):
		print('Eat meat...')
		
class HerbivoresMixin(object):
	def Her(self):
		print('Eat glass...')
		
class Bird(Animal):
	pass
	
class Dog(Mammal, RunnableMixin, CarnivorousMixin):
	pass
	
class Bat(Mammal, FlyableMixin, HerbivoresMixin):
	pass
	
class Parrot(Bird):
	pass
	
class Ostrich(Bird):
	pass
	
dog = Dog()
dog.run()
dog.Car()
dog.fly()
dog.Her()