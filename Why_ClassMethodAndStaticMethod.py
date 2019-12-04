
class Company(object):
	def foo(self, arg1):
		print('Executing: {}, {}'.format(self, arg1))

	@classmethod
	def class_foo(cls, x):
		print('Executing: {}, {}'.format(cls, x))

	@staticmethod
	def static_foo(x):
		print('Executing: {}'.format(x))



def main():
	apple = Company()

	# With object instance
	apple.foo(1)

	# With classmethod
	## We intend to do call the function from class level, 
	## rather than the instance level
	apple.class_foo(1)
	Company.class_foo(1)

	# With staticmethod
	## Neither self or cls is passed to the function, 
	## this function behaves like a normal file except 
	## that it can be called from an instance or a class
	apple.static_foo(1)
	Company.static_foo(1)


	# Bounded or not Bounded?
	## i.e. foo takes 2 args, where as apple.foo only takes 1 arg.
	## `apple` is bound to `foo`
	## apple.foo returns a partially applied version of the function
	## with the object instance `apple` bounded as the first arg to the funtion
	print(apple.foo)


	## `Company` is bound to `class_foo`
	print(apple.class_foo)
	print(Company.class_foo)


	## Normal static function
	print(apple.static_foo)
	print(Company.static_foo)


if __name__ == '__main__':
    main()