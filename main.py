#Inheritance : (Single Inheritance)
#Create a Class and define its fuctions :
class Vehicle:
    def __init__(self,mileage,cost):  #Passing More than 1 Parameter, Thats why using INIT Method.
        self.mileage = mileage
        self.cost = cost

    def show_vehicle_details(self):  
        print("I am a Vehicle")
        print("Mileage of Vehice is ", self.mileage)
        print("Cost of Vehicle is ", self.cost)
class Car(Vehicle):
    def show_car_details(self):   
        print("I am a Car")
# Store the class in a variable:
c1 = Car(500,700) #Since It is having the properties of Vehicle, Car(Vehicle) --> We will pass the parameters of Vehicle only as done.
c1.show_vehicle_details()

c1.show_car_details()

