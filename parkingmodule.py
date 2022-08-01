from abc import ABC,abstractmethod
import datetime

class Base(ABC):
    @abstractmethod
    def showInfo():
        pass

#-----------------------------------------------------------------------------------   

class Parking(Base):
    placeCode=1
    receptionCode=1

    def __init__(self, parkingName, starTime,endTime,inputPrice,owner):
      self.__parkingName = parkingName
      self.__starTime = starTime
      self.__endTime = endTime
      self.__inputPrice=inputPrice
      self.__owner=owner 
      self.__floors=[]

    def getFloors(self):
        return self.__floors

    def addFloor(self,floor):
        self.__floors.append(floor)

    def deleteFloor(self,floor):
        self.__floors.remove(floor)

    def changeInputPrice(self,newInputPrice):
        self.__inputPrice=newInputPrice

    def editParkingInfo(self, newParkingName, owner):
        self.__parkingName = newParkingName
        self.__owner=owner 

    @property
    def starTime(self):
        return self.__starTime

    @starTime.setter
    def starTime(self,starTime):
        self.__starTime=starTime

    @property
    def endTime(self):
        return self.__endTime

    @endTime.setter
    def endTime(self,endTime):
        self.__endTime=endTime

    def __str__(self) :
        return f"Parking : {self.__parkingName} \t\t Owner : {self.__owner} \t\t Number of Floor : {len(self.__floors)}\nStarTime : {self.__starTime} \t\t endTime : {self.__endTime} "

    def showInfo(self):
        print("Parking Info Is : \n---------------------------------------------")
        print(self)

#-----------------------------------------------------------------------------------
class Floor(Base):
    def __init__(self,floorName):
      self.__floorName = floorName
      self.__parts = []                      

    def __str__(self) :
        tempStr=""
        i=1
        for part in self.__parts:
            tempStr+=str(i)+"_"+str(part)+"\n"
            i+=1
        return f"FloorName : {self.__floorName}\n{tempStr}"

    @property
    def floorName(self):
        return self.__floorName

    @floorName.setter
    def floorName(self,floorName):
        self.__floorName=floorName

    @property
    def parts(self):
        return self.__parts



    def showInfo(self):
        print("Floor Info Is : \n---------------------------------------------")
        print(self)

    def addPart(self,part):
        self.__parts.append(part)
    
    def deletePart(self,part):
        self.__parts.remove(part)

    def showParts(self):
        for part in self.__parts:
            print(part)

#-----------------------------------------------------------------------------------
class Part(Base):
    def __init__(self, partName, capacity):
      self.__partName = partName
      self.__capacity = capacity
      self.__places=[]

    def __str__(self) :
        return f"{self.__partName}\t\tCapacity : {self.__capacity} "
        
    @property
    def partName(self):
        return self.__partName

    @partName.setter
    def partName(self,partName):
        self.__partName=partName

    @property
    def places(self):
        return self.__places

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self,capacity):
        self.__capacity=capacity

    def addPlace(self,place):
        self.__places.append(place)

    def getListOfEmptyPlace(self,placeType):
        return [place for place in self.__places if place.placeState==False and place.placeType==placeType]

    def __showPlacesInfo(self):
        for place in self.places:
            print(place)

    def showInfo(self):
        print("Part Info Is : \n---------------------------------------------")
        print(self)
        print("Places : ")
        self.__showPlacesInfo()
        
#-----------------------------------------------------------------------------------
class PlaceType:
    def __init__(self, placeTypeName, price):
      self.placeTypeName = placeTypeName
      self.price = price

    def __str__(self):
        return f"{self.placeTypeName}\t\t{self.price}"

    def changePlaceTypePrice(self,newPrice):
        self.price=newPrice


#-----------------------------------------------------------------------------------
class Place(Base):
    def __init__(self,placeType,placeCode):
        self.__placeCode=placeCode  
        self.__placeType=placeType
        self.__placeState=False

    def __str__(self) :
        return f"Code : {self.__placeCode}   - Type : {self.__placeType} - State : {self.__placeState} "

    @property
    def placeCode(self):
        return self.__placeCode

    @property
    def placeState(self):
        return self.__placeState

    @placeState.setter
    def placeState(self,placeState):
        self.__placeState=placeState   


    @property
    def placeType(self):
        return self.__placeType


    def changePlaceType(self,newPlaceType):
        self.__placeType=newPlaceType

    def changePlaceState(self):
        self.__placeState=not self.__placeState  

    def showInfo(self):
        print("Place Info Is : \n---------------------------------------------")
        print(self)

#-----------------------------------------------------------------------------------
class Car(Base):
    def __init__(self,plaque,carType):
        self.__plaque=plaque
        self.__carType=carType

    def __str__(self):
        return f"plaque{self.__plaque}\t\tCarType : {self.__carType}"

    def showInfo(self):
        print("Car Info Is : \n---------------------------------------------")
        print(self)

#-----------------------------------------------------------------------------------
class  Reception:
    def __init__(self,receptionCode,plaque,placeCode,subscriptionCode=0):
        self.__receptionCode= receptionCode
        self.__placeCode=placeCode
        self.__plaque=plaque
        self.__dateIn=datetime.datetime.now()
        self.__dateOut=datetime.datetime.now()
        self.__subscriptionCode=subscriptionCode


    def __str__(self):
        return f"code : {self.__receptionCode}\t\tPlaque : {self.__plaque}\t\tPlaceCode : {self.__placeCode}\nDateIn : {self.__dateIn}\t\tDateOut : {self.__dateOut}"

    def changeDateOut(self,h):
        self.__dateOut=self.__dateOut+datetime.timedelta(hours=h)
        
    def hoursdiff(self):
        return abs((self.__dateOut - self.__dateIn).total_seconds())/3600

