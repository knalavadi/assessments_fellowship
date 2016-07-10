# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 


def item_cost(tax, state_abbrev, cost):
	if state_abbrev == 'CA':
		tax = .070
		# return tax * cost
	else:
		tax = .050	
	return "$"+ str((tax * cost) + cost)

print "\n=== Part One ===\n"
print "the item in California costs " + item_cost(9,'CA',400)	
print "the item in Nevada costs " + item_cost(9,'NV',400) + "\n"

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit_name):

	fruit_name = str(fruit_name)
	if (fruit_name == "cherry" or fruit_name == "strawberry" or fruit_name == "blackberry"):
		return True 
	else:
		return False	
print "=== Part Two === \n1.a)"
print is_berry("blackberry") 
print is_berry("apple")


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit_name):
	if is_berry(fruit_name) == True:
		return 0 
	else:
		return 5

print "\n1.(b)"
print shipping_cost("blackberry")
print shipping_cost("apple")					

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
	town_name = str(town_name)
	if town_name == "Sacramento":
		return True
	else:
		return False 	

print "\n2.(a)"
print is_hometown("Seattle")
print is_hometown("Sacramento")

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first, last):
	first = str(first)
	last = str(last)
	return first + " " + last

print "\n2.(b)"
print full_name("krisha", "nalavadi")
print full_name("Sherlock", "Holmes")



#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(hometown, firstname, lastname):
	if is_hometown(hometown) == True: 
		print "Hi " + full_name(firstname, lastname) + " we're from th same place!"
	else:
		print "Hi " + full_name(firstname, lastname) + " we're from different places"

print "\n2.(c)"
print hometown_greeting("Santa Barbara", "Heidi", "Stevens")
print hometown_greeting("Sacramento", "Paulo", "Balducci")



#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################


def increment(x):
	def add(y):
		return x + y
	return add	

adding = increment(1)
print "\n=== PART Three === \n1. "
print adding(7)		

print"\n2."
add5 = increment(5)
print add5(5) 
print add5(20)


def adding_list(num1,num_list):
	list_new = [num_list]
	list_new.append(num1)
	return list_new

print "\n3."
print adding_list(2, 1)


















