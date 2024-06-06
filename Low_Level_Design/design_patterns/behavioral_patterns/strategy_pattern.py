class Transport:
    s = 10
    def __init__(self, strategy):
        self.strategy = strategy
    
    def courier(self, order):
        return self.strategy(order)
    
def airTransport(order):
    print(f"{order} couriered via air-transport")

def roadTransport(order):
    print(f"{order} couriered via road-transport")

def waterTransport(order):
    print(f"{order} couriered via water-transport")

#client
order1 = Transport(airTransport)
order1.courier("television")

order2 = Transport(roadTransport)
order2.courier("fridge")

order3 = Transport(waterTransport)
order3.courier("bike")