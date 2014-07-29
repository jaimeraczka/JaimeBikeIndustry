from BicycleIndustry.py import *



RoadWheel = Wheel(2,5,"RoadWheel")
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
JoceBikeShop.bike_shop_inventory(Bike1,Bike2,Bike3,Bike4,Bike5,Bike6)
JoceBikeShop.bike_shop_profit = 0.20

CustJudy = Customer("CustJudy",200)
CustLiz = Customer("CustLiz", 500)
CustAndrea = Customer("CustAndrea",1000)

print Bike1.bike_name, Bike1.bike_weight
print Bike2.bike_name, Bike2.bike_weight
print Bike3.bike_name, Bike3.bike_weight
print Bike4.bike_name, Bike4.bike_weight
print Bike5.bike_name, Bike5.bike_weight
print Bike6.bike_name, Bike6.bike_weight


## I should be able to make a "for" loop to execute these three things, but I'm not sure what they're "in"
print CustJudy.cust_name " can afford the following bikes: "
for bike in bike_shop_inventory:
	where bike_shop_price <= CustJudy.cust_funds
	print bike_name

print CustLiz.cust_name " can afford the following bikes: "
for bike in bike_shop_inventory:
	where bike_shop_price <= CustLiz.cust_funds
	print bike_name

print CustAndrea.cust_name " can afford the following bikes: "
for bike in bike_shop_inventory:
	where bike_shop_price <= CustAndrea.cust_funds
	print bike_name

print JoceBikeShop.bike_shop_name "has the following bikes as opening inventory:", bike_shop_inventory

for Customer:
	print cust_name "purchased %s for %s, and has %s leftover" % (bike_name,bike_shop_price,cust_funds-bike_shop_price)

## PUT WHO BOUGHT WHAT BIKE WHERE HERE. 

## PRINT OUT REMAINING INVENTORY
## PRINT OUT PROFIT



