#class and inheritance 
# as an object-orinted programming language, python supports a full range of features, such as inheritance, polymorphism and encapsulation
# user defined class is object of other meta class (meta class is collection of claasss)

# example:
#        say you want to record the grades of a set of students whose name aren't known in advance.
#        i.e


# class FoodDrinks(cammel case)

# class car:
# 	pass
# # dir(car)
# # callable(car)
# c = car()
# print(car)#on calling classs obj formed
# print(c)#
# d = b()
# print(b)
# print(d)
# e = d
# print(e)




# class car:
# 	pass
# class bike:
# 	pass


# c = car()
#  isinstance(c, car)
# # print(isinstance(car, type))
# # print(isinstance(bike, type))





# Fruit = type('Fruit',(),{})
# # print(dir(Fruit))
# print(isinstance(Fruit, type))


# import sys
# class car:
# 	pass
# c = car()
# print(c.__dict__)
# c. name = 'ef20'
# print(c.__dict__)

# # import sys

# print(sys.getsizeof(car))


# class car:
# 	pass

# h = car()
# h.band = 'honda'
# y = car()
# y.brand = 'yamaha'
# print(y.__dict__, h.__dict__)


 #(init is not constructer)
# class car:
# 	def __init__(self,brand): 
# 		self.brand = brand


# h = car('honda')
# y = car('yamaha')
# print(y.__dict__,h.__dict__)


class car:
	def __init__(self, brand, modle):
		self.brand = brand
		self.modle = modle
		self.status = False
		
	def start(self):
		self.status = True

	def stop(self):
		self.status = False

h = car('honda', 'm220')
y = car('yamaha', 'm300')
print(y.__dict__,h.__dict__)
h.start()
print(y.__dict__,h.__dict__)
h.stop()
print(y.__dict__,h.__dict__)


#############################(face book page name python user group in nepal) ##############(python web page name pythonpedia)



#class and inheritance 
# as an object-orinted programming language, python supports a full range of features, such as inheritance, polymorphism and encapsulation
# user defined class is object of other meta class (meta class is collection of claasss)

# example:
#        say you want to record the grades of a set of students whose name aren't known in advance.
#        i.e


# class FoodDrinks(cammel case)

# class car:
# 	pass
# # dir(car)
# # callable(car)
# c = car()
# print(car)#on calling classs obj formed
# print(c)#
# d = b()
# print(b)
# print(d)
# e = d
# print(e)




# class car:
# 	pass
# class bike:
# 	pass


# c = car()
#  isinstance(c, car)
# # print(isinstance(car, type))
# # print(isinstance(bike, type))





# Fruit = type('Fruit',(),{})
# # print(dir(Fruit))
# print(isinstance(Fruit, type))


# import sys
# class car:
# 	pass
# c = car()
# print(c.__dict__)
# c. name = 'ef20'
# print(c.__dict__)

# # import sys

# print(sys.getsizeof(car))


# class car:
# 	pass

# h = car()
# h.band = 'honda'
# y = car()
# y.brand = 'yamaha'
# print(y.__dict__, h.__dict__)


 #(init is not constructer)
# class car:
# 	def __init__(self,brand): 
# 		self.brand = brand


# h = car('honda')
# y = car('yamaha')
# print(y.__dict__,h.__dict__)


class car:
	def __init__(self, brand, modle):
		self.brand = brand
		self.modle = modle
		self.status = False
		
	def start(self):
		self.status = True

	def stop(self):
		self.status = False

h = car('honda', 'm220')
y = car('yamaha', 'm300')
print(y.__dict__,h.__dict__)
h.start()
print(y.__dict__,h.__dict__)
h.stop()
print(y.__dict__,h.__dict__)


#############################(face book page name python user group in nepal) ##############(python web page name pythonpedia)



