from random import randint
import pygal
import matplotlib.pyplot as plt
class Die():
	
	def __init__(self,num_sides=6):
		
		self.num_sides = num_sides
		
	def roll(self):
		return randint(1,self.num_sides)
		
die = Die(8)
die1 = Die(8)

results = []
for roll_num in range(1000000):
	result = die.roll()+die1.roll()
	results.append(result)

max_result = die.num_sides+die1.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

x_values = list(range(2,17))
y_values = frequencies
plt.scatter(x_values,y_values)
plt.show()


