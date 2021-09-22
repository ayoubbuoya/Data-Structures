''' 
	Well, I'm writing this code just for me to applying what i learn from data structures course that I'm taking it.
	So, I'm not an expert.I just want to  share my progress with you guys.
	But You can ask me if you are beginner like I am and will help you if i know the answer.
	I made this code with a lot of comments to simplify it for me and for you. 
	You Can Contact Me On  : 
			Facebook : 
			GitHub : 
			Linkeldin :  
'''


class Node : 
	def __init__(self, data) :
		self.data = data
		self.pref = None #pref => Previous Node Reference 
		self.nref = None #nref => Next Node Reference 
class DoublyLinkedList :
	def __init__(self) :
		self.head = None
	#Just For Me To simplify things 
	# def loop_doubly_linked_list_forward(self) :
	# 	node = self.head 
	# 	while node is not None :
	# 		print(node.data,"====>",end=" ")
	# 		node = node.nref
	
	''' Traversal Operation '''
	#traverse forward
	def print_doubly_linked_list_forward(self) : 
		if self.head is None : 
			print("Doubly Linked List Is Empty!")
		else : 
			node = self.head
			while node is not None :
				#This If Condition Is Just For Pretty Printing The Last Node Of  Linked List
				if node.nref is None : 
					print(node.data)
					return
				print(node.data,"====>",end=" ")
				node = node.nref
	#trasverse backward
	def print_doubly_linked_list_backward(self) :
		if self.head is None : 
			print("Doubly Linked List Is Empty!")
		else : 
			node = self.head 
			while node.nref is not None : 
				node = node.nref 
			#Now, the Node is the last node 
			while node is not None :
				#This If Condition Is Just For Pretty Printing The Last Node Of  Linked List 
				if node.pref is None : 
					print(node.data)
					return
				print(node.data,"====>",end=" ")
				node = node.pref
	#This is the original Tasvere function and it takes 1 parameter (reverse) 
	#the default value is False => Print in the normal order (forward)
	#if you change it to true , it will be print the list reversally (backword)
	def print_doubly_linked_list(self, reverse=False) :
		if reverse == False : 
			self.print_doubly_linked_list_forward()
		else : 
			self.print_doubly_linked_list_backward()
	''' Inserion Operation '''
	#Add To An Empty soubly linked list 
	def add_to_empty(self, data="empty_value") : 
	 	if self.head is None : 
	 		new_node = Node(data) 
	 		self.head = new_node
	 	else : 
	 		print("\nDoubly Linked List Is Not Empty!!")
	#add From THe Begin 
	def add_to_begin(self, data="begin_value") :
		new_node = Node(data)
		if self.head is None : 
			self.head = new_node
		else : 
			first_node = self.head
			new_node.nref = self.head
			first_node.pref = new_node
			self.head = new_node
	#add To The End 
	def add_to_end(self, data="end_value") :
		new_node = Node(data)
		if self.head is None : 
			self.head = new_node
		else : 
			node = self.head
			while node.nref is not None : 
				node = node.nref 
			last_node = node
			last_node.nref = new_node 
			new_node.pref = last_node
	#Insert before a given node 
	def add_before_node(self, data, given_node_data) :
		#Check if the list is empty or not 
		if self.head is None : 
			self.add_to_empty(data)
		elif self.head.data == given_node_data : 
			self.add_to_begin(data)
		else : 
			node = self.head
			while node is not None :
				if node.data == given_node_data :
					break
				node = node.nref
			if node is None : 
				print('Given Node Data Is Not Present In DLL.') 
			else : 
				new_node = Node(data)
				new_node.pref = node.pref
				new_node.nref = node  
				node.pref.nref = new_node
				node.pref = new_node
	#Insery after a given node 
	def add_after_node(self, data, given_node_data):
		if self.head is None : 
			print("Doubly Linked List Is Empty !!")
		else : 
			node = self.head
			while node is not None : 
				if node.data == given_node_data : 
					break 
				node = node.nref
			if node is None : 
				print('Given Node Data Is Not Present In DLL.')
			else : 
				new_node = Node(data)
				new_node.nref = node.nref 
				new_node.pref = node
				if node.nref is not None : #If Condition that run when we aren't in the last Node
					node.nref.pref = new_node
				node.nref = new_node 
	''' Deletion  Operation '''
	def delete_from_begin(self) :
		if self.head is None : 
			print("Doubly Linked List Is Empty!.Can't Delete")
		else : 
			if self.head.nref is None : 
				self.head = None 
				print("Doubly Linked List Is Empty after deleting the node!")
				return
			self.head = self.head.nref
			self.head.pref = None
	def delete_from_end(self) :
		if self.head is None  : 
			print("Doubly Linked List Is Empty.Can't Delete!")
		elif self.head.nref is None : 
			print("Doubly Linked List Is Empty after deleting the node!")
			self.head = None 
		else : 
			node = self.head 
			while node.nref is not None : 
				node = node.nref
			node.pref.nref = None
	def delte_by_value(self, given_value) :
		if self.head is None : 
			print("Doubly Linked List Is Empty.Can't Delete!")
		elif self.head.nref is None : 
			print("Doubly Linked List Is Empty after deleting the node!")
			self.head = None 
		elif self.head.data == given_value : 
			self.delete_from_begin()
		else : 
			node = self.head 
			while node is not None : 
				if node.data == given_value : 
					node.pref.nref = node.nref
					if node.nref is not None : 
						node.nref.pref = node.nref
					return 
				node = node.nref




''' Insertion  Test '''
dll1 = DoublyLinkedList()
dll1.add_to_empty(60)
dll1.add_to_begin(50)
dll1.add_to_begin(40)
dll1.add_to_begin(30)
dll1.add_to_begin(20)
dll1.add_to_begin(10)
dll1.add_to_end(70)
dll1.add_to_end(80)
dll1.add_to_end(90)
dll1.add_to_end(100)
dll1.add_before_node(25,30)
dll1.add_after_node(35,30)
dll1.add_before_node(45,50)
dll1.add_before_node(55,60)
dll1.add_after_node(65,60)
dll1.print_doubly_linked_list()
print('')
dll1.print_doubly_linked_list(reverse=True)

''' Deletion Tests ''' 
dll2 = DoublyLinkedList()
dll2.add_to_begin(50)
dll2.add_to_begin(40)
dll2.add_to_begin(30)
dll2.print_doubly_linked_list()
dll2.delete_from_begin()
dll2.delete_from_begin()
dll2.delete_from_begin()
dll2.print_doubly_linked_list()
dll2.add_to_begin(50)
dll2.add_to_begin(40)
dll2.add_to_begin(30)
dll2.print_doubly_linked_list()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.print_doubly_linked_list()
dll2.add_to_empty(60)
dll2.add_to_begin(50)
dll2.add_to_begin(40)
dll2.add_to_begin(30)
dll2.add_to_begin(20)
dll2.add_to_begin(10)
dll2.add_to_end(70)
dll2.add_to_end(80)
dll2.add_to_end(90)
dll2.add_to_end(100)
dll2.print_doubly_linked_list()
dll2.delte_by_value(100)
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delete_from_end()
dll2.delte_by_value(10)
dll2.print_doubly_linked_list()
