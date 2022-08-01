import parkingmodule as pm
from functionmodule import searchEmptyPlace
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
parking=pm.Parking("Arya",8,21,2000,"abbasi")



floor0=pm.Floor("Tabaghe Hamkaf")
floor1=pm.Floor("Tabaghe Aval")
# floor2=pm.Floor("Tabaghe Dovom")
# floor3=pm.Floor("Tabaghe Sevom")



floor0.addPart(pm.Part("SalonA",3))
floor0.addPart(pm.Part("SalonB",3))

floor1.addPart(pm.Part("SalonA",3))
floor1.addPart(pm.Part("SalonB",5))
floor1.addPart(pm.Part("SalonC",3))

# floor2.addPart(pm.Part("SalonA",3))
# floor2.addPart(pm.Part("SalonB",5))
# floor2.addPart(pm.Part("SalonC",3))

# floor3.addPart(pm.Part("SalonA",3))
# floor3.addPart(pm.Part("SalonB",5))
# floor3.addPart(pm.Part("SalonC",3))



parking.addFloor(floor0)
parking.addFloor(floor1)
# parking.addFloor(floor2)
# parking.addFloor(floor3)


public=pm.PlaceType("Omoumi",5000)
private=pm.PlaceType("Khosousi",12000)

for part in floor0.parts:
    for i in range(0,part.capacity):
        part.addPlace(pm.Place(public,parking.placeCode))
        parking.placeCode+=1


for part in floor1.parts:
    for i in range(0,part.capacity):
        part.addPlace(pm.Place(private,parking.placeCode))
        parking.placeCode+=1



for floor in parking.getFloors():
    floor.showInfo()
    for part in floor.parts:
        part.showInfo()
    print("#####################################################")




emptyPlace=searchEmptyPlace(parking,public)
r1=pm.Reception(parking.receptionCode,"24654-IR28",emptyPlace.placeCode)
print(r1)
print("==========================================")
r1.changeDateOut(2)
print(r1)
print(r1.hoursdiff())


emptyPlace=searchEmptyPlace(parking,private)
r2=pm.Reception(parking.receptionCode,"434657-IR11",emptyPlace.placeCode)
print(r2)
print("==========================================")
r2.changeDateOut(6)
print(r2)
print(r2.hoursdiff())




for floor in parking.getFloors():
    floor.showInfo()
    for part in floor.parts:
        part.showInfo()
    print("#####################################################")









# emptyPlace=searchEmptyPlace(parking)
# print(emptyPlace)
# emptyPlace=searchEmptyPlace(parking)
# print(emptyPlace)

# r1=pm.Reception(parking.receptionCode,emptyPlace.placeCode)
# parking.receptionCode+=1
# print(r1)
# r1.changeDateOut(3)
# print(r1)
# print(r1.hoursdiff())

