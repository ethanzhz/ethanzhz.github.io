class Butt:
    def __init__(self, cont, fac):
        self.cont = cont
        self.fac = fac


class Car:
    def __init__(self, fac, butt):
        self.fac = fac
        self.butt = butt

b = Butt(100, 'byd')
car = Car('mi', b)

print(car.fac)
print(car.butt.fac)