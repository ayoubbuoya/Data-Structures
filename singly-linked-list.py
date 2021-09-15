class Node :
	def __init__(self, data) :
		self.data = data
		self.ref = None
class LinkedList() : 
	def __init__(self):
		self.head = None
	''' Trasversal Operation '''
	def print_LinkedList(self) :
		if self.head is None : 
			print("Linked List Is Empty!")
		else : 
			node = self.head 
			while node is not None :
				print(node.data,"====>",end=" ")
				node = node.ref
	''' Inserion Operation ''' 
	#add From THe Begin 
	def add_to_begin(self, data) :
		new_node = Node(data)
		new_node.ref = self.head
		self.head = new_node 
	def add_to_end(self, data) :
		new_node = Node(data)
		if self.head is None :		#First node  
			self.head = new_node
		else : 
			node = self.head
			while node.ref is not None : #Looping To Reach The Last Node Reference
				node = node.ref
			node.ref = new_node
	#Add After The Given Node 
	def add_after_node(self, data, given_node_data) : #given node data is a variable that refers to the data of node that we want to add the new node after it 
		node = self.head
		while node is not None :
			if node.data == given_node_data : 
				break 
			node = node.ref		#We Use It Break So THat Means No Need For Else Statment because It Will Automaticly break the whole looop 
		if node is None : 
			print("Node Is Not Present In Linked List!")
		else : 
			new_node = Node(data)
			new_node.ref = node.ref
			node.ref = new_node
	#Add Before The Given Node 
	def add_before_node(self, data, given_node_data) : 
		#check if the linked list is empty *
		if self.head is None : 
			print("Linked List Is Empty!!")
			return  #exiting the method 
		#Checking if the first node is teh given node that we want to add before it
		if self.head.data == given_node_data : 
			self.add_to_begin(data)
			return  #Return Used For bREAK THE CODE 
		node = self.head 
		while node.ref is not None : 
			if node.ref.data == given_node_data :  #finding the prev node 
				break 
			node = node.ref
		if node.ref is None :
			print("Node Is Not Present In This Linked List!")
		else : 
			#create a node 
			new_node = Node(data)
			new_node.ref = node.ref
			node.ref = new_node
	#Add To An Empty Linked List 
	def add_to_empty(self, data):
		if self.head is None : 
			new_node = Node(data)
			self.head = new_node
		else : 
			print("Linked List Is Not Empty!!")
	''' Deletion Operation ''' 
	# Delete From The Begin 
	def delete_from_begin(self):
		if self.head is None : 
			print("You Cannot Delete Nodes From An Empty Linked List.")
		else :
			first_node = self.head 
			self.head = first_node.ref 
	# Delete From The End
	def delete_from_end(self):
	 	if self.head is None : 
	 		print("You Cannot Delete Nodes From An Empty Linked List.")
	 	elif self.head.ref is None : 
	 		self.head = None
	 	else :
	 		node = self.head
	 		#Access To The nex Node 
	 		while node.ref.ref is not None : 
	 			node = node.ref
	 		node.ref = None
	# Delete By Value 
	def delete_by_value(self, given_value) :
		#Check if the list is empty or not  
		if self.head is None : 
			print("You Cannot Delete Nodes From An Empty Linked List.")
		#check if the givven value is the first node in linked list
		elif self.head.data == given_value :
		 	self.delete_from_begin() 
		#delete by value 
		else : 
			node = self.head
			while node.ref is not None :
				if node.ref.data == given_value : 
					node.ref = node.ref.ref
				else :
					node = node.ref






''' Some Tests '''

LL1 = LinkedList()
LL1.add_to_begin(30)
LL1.add_to_begin(30)
LL1.add_to_begin(30)
LL1.add_to_begin(30)
LL1.add_to_begin(30)
LL1.add_to_begin(80)
LL1.add_to_begin(50)
LL1.add_to_begin(30)
LL1.add_to_begin (20)
LL1.add_to_begin(40)
LL1.print_LinkedList()
print("")
LL1.delete_by_value(20)
LL1.print_LinkedList()
