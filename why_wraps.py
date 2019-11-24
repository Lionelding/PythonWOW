import click
from functools import wraps

@click.group()
def run():
    pass


def logging(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		# import pdb;pdb.set_trace()
		print('name: '+func.__name__)
		print('docstring: ' + func.__doc__)
		return func(*args, **kwargs)
	return with_logging


@logging
def f(arg):
	"""
	This docstring belongs to f.
	"""
	res = arg + arg 
	print(res)
	return res


def main():
	# Objective: Validat the usage of @wraps
	# By adding @wraps, the original information from the func is automatically copied here. 
	# i.e. __name__, __doc__, 
	f(1)


if __name__ == '__main__':
    main()