from pen import Pen
class Farm:

    def __init__(self, id, name, city, state, type = "cattle"):
        self.farmid = id 
        self.name = name 
        self.city = city
        self.state = state 
        self.type = type 
        self.pen = Pen()



