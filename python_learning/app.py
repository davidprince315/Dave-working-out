class HashTable:
	def __init__(self):
		self.MAX = 100
		self.arr = [[] for i in range(self.MAX)]

	def get_hash(self,key):
		h = 0
		for char in key:
			h+= ord(char)
			return h % self.MAX

	def add(self, key, val):
		h = self.get_hash(key)

		for idx, element in enumerate(self.arr[h]):
			if len(element)==2 and element[0]==key:
				self.arr[h][idx] = (key,val)
				found = True
				break
			if not found:
				self.arr[h].append((key,val))
		

	def get(self, key):
		h = self.get_hash(key)
		for element in self.arr[h]:
			if element[0] == key:
				return element[1]

	def delete(self, key):
		h = self.get_hash(key)
		for index, element in enumerate(self.arr[h]):
			if element[0] == key:
				del self.arr[h][index]



table = HashTable()
with open("nyc_weather.csv","r") as f:
	for line in f:
		tokens = line.split(',')
		day = tokens[0]
		if tokens[1].isdigit():
			temp = int(tokens[1])
		else:
			temp = tokens[1]
		table.add(day,temp)
print(table.arr)

