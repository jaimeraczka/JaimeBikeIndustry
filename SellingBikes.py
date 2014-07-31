from BicycleIndustry import *


road_wheel = Wheel(2,5,"RoadWheel")
BeachWheel = Wheel(3,8,"BeachWheel")
TrackWheel = Wheel(4,10,"TrackWheel")

Aluminum = Frame("AluminumFrame",10,100)
Carbon = Frame("CarbonFrame",12,150)
Steel = Frame("SteelFrame", 15, 200)

JoeBike = Bicycle_Manuf("JoeBike")
JeffBike = Bicycle_Manuf("JeffBike")

Bike1 = Bicycle_Model("Bike1",JoeBike,BeachWheel,Aluminum)
Bike2 = Bicycle_Model("Bike2",JoeBike,RoadWheel,Steel)
Bike3 = Bicycle_Model("Bike3",JoeBike,TrackWheel,Carbon)

Bike4 = Bicycle_Model("Bike4",JeffBike,TrackWheel,Steel)
Bike5 = Bicycle_Model("Bike5",JeffBike,RoadWheel,Aluminum)
Bike6 = Bicycle_Model("Bike6",JeffBike,BeachWheel,Carbon)


JoceBikeShop = Bike_Shop("JoceBikeShop")
JoceBikeShop.add_bike_to_inventory(Bike1)
JoceBikeShop.add_bike_to_inventory(Bike2)
JoceBikeShop.add_bike_to_inventory(Bike3)
JoceBikeShop.add_bike_to_inventory(Bike4)
JoceBikeShop.add_bike_to_inventory(Bike5)
JoceBikeShop.add_bike_to_inventory(Bike6)


CustJudy = Customer("CustJudy",200)
CustLiz = Customer("CustLiz", 500)
CustAndrea = Customer("CustAndrea",1000)

customer_list = []
customer_list.append(CustJudy)
customer_list.append(CustLiz)
customer_list.append(CustAndrea)

for some_bike in JoceBikeShop.bike_shop_inventory:
    print some_bike.bike_name, some_bike.bike_weight


for Customer in customer_list:
	print Customer.cust_name "can afford the following bikes: "
	for some_bike in bike_shop_inventory:
		where some_bike.bike_shop_price <= Customer.cust_funds
		print some_bike.bike_name
	

print JoceBikeShop.bike_shop_name "has the following bikes as opening inventory:", JoceBikeShop.bike_shop_inventory

print Customer.cust_name(CustJudy) "purchased Bike1"
JoceBikeShop.remove_bike_from_inventory(Bike1)
print Customer.cust_funds(CustJudy) - JoceBikeShop.bike_shop_price(Bike1)

print Customer.cust_name(CustLiz) "purchased Bike2"
JoceBikeShop.remove_bike_from_inventory(Bike2)
print Customer.cust_funds(CustLiz) - JoceBikeShop.bike_shop_price(Bike2)

print Customer.cust_name(CustAndrea) "purchased Bike3"
JoceBikeShop.remove_bike_from_inventory(Bike3)
print Customer.cust_funds(CustAndrea) - JoceBikeShop.bike_shop_price(Bike3)

print JoceBikeShop.bike_shop_name "has the following bikes as opening inventory:", JoceBikeShop.bike_shop_inventory

print JoceBikeShop.bike_shop_name "made a profit of: " (JoceBikeShop.bike_shop_price(Bike1) + JoceBikeShop.bike_shop_price(Bike2) + JoceBikeShop.bike_shop_price(Bike3)) * JoceBikeShop.bike_shop_profit
