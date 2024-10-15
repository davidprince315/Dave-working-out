#must create classes for Node and Linked List and manually define functions for each 
#because Nodes and linked lists aren't inherhitly found in python

#must create a class for the node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

#must create a class for the linked list
class LinkedList:
	def __init__(self):
		self.head = None

	def print(self):
		if self.head == None:
			print("List is Empty")
			return
		itr = self.head
		ll_str = " "
		while itr:
			ll_str = str(itr.data)+ '--->' if itr.next else str(itr.data)
			itr = itr.next
		print(llstr)

	def getLength(self):
		itr = self.head
		count = 0
		while itr:
			count +=1
			itr = itr.next
		print(f"The total nodes in the linked list is {count}")

	def insertBeggining(self, data):
		node = Node(data, self.head)
		self.head = node


	def insertEnd(self, data):
		if self.head is None:
			self.head = Node(data, None)
		
		itr = self.head

		while itr:
			itr = itr.next

		itr.next Node(data, None)

	def insertAt(self, index, data):
		if index < 0 or index > self.getLength():
			raise Exception("Invalid Index")

		if index == 0:
			self.insertBeggining(data)
			return

		itr = self.head
		count = 0

		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				break

			itr = itr.next
			count += 1

	def removeAt():
		if index < 0 or index > self.getLength():
			raise Exception("Invalid Index")

		if index == 0:
			self.head = self.head.next
			return

		itr = self.head
		count = 0

		while itr:
			if count == index - 1:
				itr.next = itr.next.next
				break

			itr = itr.next
			count += 1

	def insertValues():
		self.head = None
		for data in data_list:
			self.insertEnd(data)


    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()




