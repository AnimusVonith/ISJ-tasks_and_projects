# minitask 6
class Point:

	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return (x, y)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return (x, y)

p0 = Point()        
p1 = Point(3, 4)
print(p0-p1)
p2 = Point(1, 2)
result = p1-p2
print(result)