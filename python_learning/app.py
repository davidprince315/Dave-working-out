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

		for inx, element in enumerate(self.arr[h]):
			if len(element)==2 and element[0]==key:
				
		self.arr[h].append(key,val)
		

	def get(self, key):
		h = self.get_hash(key)
		return self.arr[h]

	def delete(self, key):
		h = self.get_hash(key)
		self.arr[h] = None



table = HashTable()
table.add('march 6', 130)
print(table.get('march 6'))

