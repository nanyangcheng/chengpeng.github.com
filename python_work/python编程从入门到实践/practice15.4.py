from random import randint
import pygal
class Die():
	
	def __init__(self,num_sides=6):
		
		self.num_sides = num_sides
		
	def roll(self):
		return randint(1,self.num_sides)
		
die = Die()

results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

frequencies = []
for value in range(1,die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()
hist.title="result"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "result"
hist.y_title = "frequency"

hist.add('D6',frequencies)
hist.render_to_file('div_visual.svg')	
print(frequencies)
