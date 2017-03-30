import abc

class Vehicle(object):
    __metaclass__= abc.ABCMeta
    def __init__(self):
        pass

    def __str__(self):
        return "vehicle"

    @abc.abstractmethod
    def start(self):
        """this is going to be a long
            comment"""
        raise NotImplementedError("Vehicle can't start")

class Ford(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.model = "Ford"

    def __sr__(self):
        return Vehicle.__str__(self) + "model = "\
               + self.model

    def start(self):
        print "use a key"

f1 = Ford()
print f1
#v1= Vehicle
#print v1
f1.start()
