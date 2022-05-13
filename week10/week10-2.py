from turtle import speed


class car :
    speed = 0
    color = ""
    count = 0
    
    def __init__(self) :
        self.color = "red"
        self.count += 1

    def speedUp(self, value) :
        self.speed += value
    
    def speedDown(self, value) :
        self.speed -= value

class bus(car) :
    seat = 0

    def seatUp(self, value) :
        self.seat += value

class truck(car) :
    weight = 0
    
    def weightUp(self, value) :
        self.weight += value

car1 = truck()
car2 = bus()

while(car1.speed < 100) :
    car1.speedUp(100)

while(car2.speed < 100) :
    car2.speedUp(20)

car1.weightUp(20)
car2.seatUp(5)

print("%d %d"%(car1.speed, car2.speed))
print("%d %d"%(car1.weight, car2.seat))