
def searchToPlacesListForEmptyPlace(places):
    for place in places:
        if place.placeState==False :
            return place


def searchEmptyPlace(parking,placeType):
    for floor in parking.getFloors():
        for part in floor.parts:
            places=part.getListOfEmptyPlace(placeType)
            if(len(places)>0):
                place=searchToPlacesListForEmptyPlace(places)
                place.changePlaceState()
                return place