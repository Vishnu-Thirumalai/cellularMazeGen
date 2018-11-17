import random
import sys

class mazeGeneration:

	def __init__(self, size, inital, life, death):
		self.size = size
		self.initial = 0.4
		self.done = False

		self.birthLimit = 4 
		self.deathLimit = 2

		self.neighbours = [ (x,y) for x in range(-1,2) for y in range(-1,2)]
		self.neighbours.remove((0,0))	
	
		self.map = [[ (0 if random.random()>self.initial else 1) for x in range(size)] for y in range(size)]

	def main(self):
		
		while not self.done:
			
			self.iterate()
		
		for x in range(self.size):
			self.map[0][x] = 2
			self.map[self.size-1][x] = 2
			self.map[x][0] = 2
			self.map[x][self.size-1] = 2	

		self.displayMap()	

			
	def displayMap(self):
		for row in self.map:
			for pos in row:
				print ( " " if pos==1 else pos , end = " ")
			print ("")
		print("")

	def add(self,a,b):
		return (a[0]+b[0], a[1]+b[1])

	def iterate(self):
		self.done = True
		for y in range(self.size):
			for x in range(self.size):
				val = 0
				curr = self.map[y][x]
				for bias in self.neighbours:
					n = self.add((x,y),bias)
					try:
						val = val + self.map[n[1]][n[0]]
					except IndexError:
						pass
						
				if val < self.deathLimit:
					self.map[y][x] = 0
				elif val > self.birthLimit:
					self.map[y][x] = 1	
				
				if self.map[y][x] != curr:
					self.done = False



args = [100, 0.4, 3, 4]
try:
	args[0] = int(sys.argv[1])
	args[1] = float(sys.argv[2])
	args[2] = int(sys.argv[3])
	args[3] = int(sys.argv[4])
except IndexError:
	pass	

m = mazeGeneration(*args)
m.main()							
