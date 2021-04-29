#minitask 7

def deprecated(func):
	def wrapped_func(*args):
		print("Call to deprecated function: " +func.__name__ +"\n" +str(func(*args)))
		return func(*args)
	return wrapped_func

@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,2)

# should write:
# Call to deprecated function: some_old_function
# 3