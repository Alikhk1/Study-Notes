

#  Functions :

- Just another type of object.

- Functions as Variables :
	- EXAMPLE : Assigning print function to a variable. Do not use the parenthesis, because when we use them, we're calling the function.

- Fucntions can be added to lists/Dictionaries : 
	- EXAMPLE : list[2]('Hello world') # The 3rd element had print function.

- Function can be Defined inside another Function (Nested/Inner/Helper/Child) 

- Function can be in the return statement of another Function.

--- 
#  Scope :

- Determines which variables can be accessed at different points in your code.

- Follows LEGB rule:

	- Local → inside current function.

	- Enclosing → inside enclosing functions (for nested functions, nonlocal keyword to modify the global variable).

	- Global → module-level. (global keyword, avoid using as they make testing/debugging harder)

	- Built-in → Python’s built-ins (len, range, etc.).

- If 2 Functions are nested Python will check the scope of the parent function first.

- A closure in Python is a function that remembers variables from its enclosing scope, even after that scope has finished executing.
	- Python attaches any non-local variables that a nested function needs to function object, those variables are stored in __closure__

--- 
#  Decorators :


- Wrapper that you can place around a function, that changes its behaviour.

- It can modify the inputs, outputs and the function itself.

- They're just functions that take another function as input.

- @ is a convention for passing that function to the decorator function.

- SYNTAX :
	def print_return_type(func):
  		def wrapper(*args, **kwargs): # Define wrapper(), the decorated function
    			result = func(*args, **kwargs) # Call the function being decorated
			# CODE TO DO SOMETHING
    			return result
  		# Return the decorated function
  		return wrapper

- DECORATOR IS ONLY SUPPOSED TO TAKE ONE ARGUMENT, THE FUNCTION IT'S DECORATING.

- DECORATOR FACTORY : FOR A DECORATOR TO TAKE MORE THAN AN ONE ARGUMENT TURN IT INTO A FUNCTION THAT RETURNS A DECORATOR RATHER THAN IS A DECORATOR 
	- SYNTAX : 
		def decorator_factory(arg1, arg2):
   		"""This factory takes arguments and returns a decorator."""

    			def actual_decorator(func):
        			@wraps(func)
        			def wrapper(*args, **kwargs):
          				  # Do something before
          				  print(f"Decorator args: {arg1}, {arg2}")
           				  print("Before function call")

            				  result = func(*args, **kwargs)

           				  # Do something after
            				  print("After function call")
            				  return result
       				return wrapper
    			return actual_decorator


- SOME USEFULL DECORATORS :
	- @timer : Find bottlenecks in code
	- @memoize : Instead of running the function on same arguments again, the answer is lookedup.

- WHEN TO USE DECORATORS : 
	- Want to add common behaviour to multiple functions.

- DECORATORS HIDE THE ATTRIBUTES OF THE FUNCTION THEY'RE USED ON (WRAPPER OVERWRITES) :
	- from functools import wraps
	- @wraps(func) #above wrapper function in decorator.

- CALL UNWRAPPED FUNCTIONED IF DECORATOR USED :
	- function.__wrapped__(arguments)


---
#  Context Managers :

- Sets up context, runs the code and ends the context.
	
- Technically a generator, that yields a single value.

- WHEN TO USE? : When code follows pattern of Open/Close, Lock/Release, Change/Reset, Enter/Exit, Connect/Disconnect, Lock/Release

- SYNTAX :
	with <context-manager>(<args>) as <variable-name>:
	
- Two ways to define a context Manager :
	1. Class
	2. Function : 
		1. @contextlib.contextmanager
		2. Define a function.
		3. Add any code inside that you need.
		4. yield Keyword - You return a value, but also expect to complete the rest of the function after it, at some time.

---

#  Nested Context :

- Nested "with" statements are perfectly legal.

--- 
#  Error Handling :
- try:  code that might raise an error.
- except: do something about the error.
- finally: this code runs no matter what.










































