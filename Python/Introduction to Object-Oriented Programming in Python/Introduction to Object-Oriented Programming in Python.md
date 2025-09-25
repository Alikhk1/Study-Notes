
- Procedural Programming : Simple sequence of steps. E.g: Data Analysis.

- Conventions : 
	1. CamelCase for Class Names.
	2. lower_snake_case for Attributes & Methods.
	3. Use DocStrings.
	4. Class Attributes : CAPITAL_CASE

- Object = data + functionality

	1. State (Attributes) : Object's data.
		
		- Class Attributes : Data Shared amoung all the instances of a Class. (Global Varaible within a Class)

			- <classname>.ATTRIBUTE_NAME to access it.
			- Set Global Constants (Minimum/Maximum Values)
			- Commonly Used Values, Configurations (port, host)

	2. Behaviour (Methods) : Object's functionality.

		- dir() - To display all attributes and methods of an object/class.

		- Class Methods : Don't have access to instance level attributes.
			- Declare with @classmethod 
			- First argument is "cls" refering to the class.
			- <classname>.method_name to access it.
			- Used to create alternate constuctors.


- Classes : Blueprint for objects outlining possible states and behaviors.

	- SYNTAX :

		1. Empty Class : 
			class <name> :
		 		pass
		
		2. Create an Object :
			Variable = Classname()


- SELF keyword : Stand in for the future Object not yet created.
	
	- It's a convention, the first argument is always treated as the object reference.


- CONSTRUCTOR : Add data to the object when creating it.
		- __init__() automatically called everytime an object is created.


---

#  Core Principles Of OOP :


1. Encapsulation : Bundling of Data & Methods.
2. Inheritance : Extend functionality of existing code. It's the essence of OOP. Code reuse.
3. Polymorphism : Enables access to different types of object, through the same interface.


---

#  Inheritance :

- SYNTAX :
	
	- class Children(ParentClass) : 
		pass 

	- CUSTOMIZATION : 
		class Children(ParentClass) :
			def __init__(self, x, y) :
				ParentClass.__init__(self, x) # Call parent constructor, we aren't required to call it. But almost always do.
				self.y = y # Additional attribute

---

#  Comparison of Objects :


1. Equality :
	- __eq__() is called when 2 Objects of a Class are compared using ==
	- Accepts Two arguments = self & other.
	- Returns True or False.

	- SYNTAX :
		def __eq__(self, other) :
			return (self.id == other.id) and (self.name == other.name) and (type(self) == type(other)) # Ensures 2 objects are of the same Class

- Python will always call the Child's eq method.


---

#  Displaying Objects :


1. __str__() : Like print(), Gives an informal representation that is suitable for end-user. String representation.

2. __repr__() : repr gives output used by developers. Reproduce, Represent.
	- Best Practice : Use repr to product a string that be used to reproduce the object.
	- It's also a fallback for print when str is not defined.
	
	- SYNTAX :

		def __repr(self):
			return f"Customer('{self.name}', {self.balance})"


---

#  Custom Exceptions :


- SYNTAX :
	
	def CustomException(Exception):
		pass

	- Now you can raise a "CustomException"

































