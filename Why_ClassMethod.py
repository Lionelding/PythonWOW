
class Cowboy(object):
	def __init__(self, single_skill):
		self.skills = single_skill

	@classmethod
	def alternative__init(self, multi_skill):
		cowboy_instance = Cowboy('')
		cowboy_instance.skills = ','.join(i for i in multi_skill) 
		return cowboy_instance

	def __repr__(self):
		return self.skills


def main():

	# One of the use cases of classmethod is to define alternative constructor
	Spike = Cowboy('eat')
	print(Spike)
	Jet = Cowboy.alternative__init(['eat', 'fight', 'fly'])
	print(Jet)

if __name__ == '__main__':
    main()