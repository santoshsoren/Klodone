
class uber:
    def __init__(self,car):
        self.car = car
        
    def sedan(self):
        self.rate = 12
        return self.rate

    def mini(self):
        self.rate = 8
        return self.rate

    def micro(self):
        self.rate = 6
        return self.rate

    def share(self):
        self.rate = 4
        return self.rate

    def time(self):
        self.rate_per_minute = 1
        return self.rate_per_minute

class Totaltime(uber):
    def __init__(self,car,travell_time):
        uber.__init__(self,car)
        self.travell_time = travell_time

    def total_time_charge(self):
        return uber.time(self)*self.travell_time

class distance(Totaltime):
    def __init__(self,car,travell_time,km):
        Totaltime.__init__(self,car,travell_time)
        self.km = km

    def getdistance(self):
        return self.km

class fare(distance):
    def __init__(self,car,travell_time,km):
        distance.__init__(self,car,travell_time,km)

    def pricing(self):
        if self.car == 1:
            price = self.km*uber.sedan(self)+Totaltime.total_time_charge(self)
            print("Total fare is Rs. ",price)
        elif self.car==2:
            price = self.km*uber.mini(self)+Totaltime.total_time_charge(self)
            print("Total fare is Rs. ",price)
        elif self.car==3:
            price = self.km*uber.micro(self)+Totaltime.total_time_charge(self)
            print("Total fare is Rs. ",price)
        elif self.car==4:
            price = self.km*uber.share(self)+Totaltime.total_time_charge(self)
            print("Total fare is Rs. ",price)
    
   
car = int(input("Select car\n"\
                "1. Sedan\n"\
                "2. mini\n"\
                "3. micro\n"\
                "4. share\n"))

dist = int(input("Enter distance in kilometer: "))
duration = int(input("Enter duration in minutes: "))
cab = fare(car,dist,duration)

cab.pricing()


    
        
        
