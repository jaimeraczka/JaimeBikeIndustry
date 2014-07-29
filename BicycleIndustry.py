# This is all my Classes for my Bicycle Industry

class Wheel(object):
	
	def __init__(self,wheel_weight,wheel_manuf_cost,_wheel_model_name):
		self.wheel_weight = wheel_weight
		self.wheel_manuf_cost = wheel_manuf_cost
		self.wheel_model_name = wheel_model_name


class Frame(object):

	def __init__(self,frame_material,frame_weight,frame_manuf_cost):
		self.frame_material = frame_material
		self.frame_weight = frame_weight
		self.frame_manuf_cost = frame_manuf_cost


class Bicycle_Model(object):

# A bike has two of the same wheel and a frame 

	bike_weight = bike_wheel.wheel_weight * 2 
	bike_cost = bike_wheel.wheel_manuf_cost * 2 + bike_frame.frame_manuf_cost

	def __init__(self,bike_name,bike_manuf,bike_wheel,bike_frame):		
		self.bike_name = bike_name
		self.bike_manuf = bike_manuf
		self.bike_wheel = bike_wheel
		self.bike_frame = bike_frame


class Bicycle_Manuf(object):

	manuf_price = bike_cost + manuf_profit

	def __init__(self,manuf_name,):
		self.manuf_name = manuf_name
	def manuf_profit()


class Bike_Shop(object):

	bike_shop_price = manuf_price + bike_shop_profit

	def __init__(self,bike_shop_name,bike_shop_profit):
		self.bike_shop_name = bike_shop_name
		self.bike_shop_profit = bike_shop_profit
	def bike_shop_inventory():
		## WHAT IS THE CODE THAT SAYS BIKES GO HERE? 


class Customer(object):

	def __init__(self,cust_name,cust_funds):
		self.cust_name = cust_name
		self.cust_funds = cust_funds
