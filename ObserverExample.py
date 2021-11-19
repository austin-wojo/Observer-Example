from abc import ABCMeta, abstractmethod
from typing import List, overload

class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def notifyObservers(observer):
        pass

    @abstractmethod
    def attach(observer):
        pass

    @abstractmethod
    def detatch(observer):
        pass


class Subject(IObservable):
    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)

    def detatch(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(*args)


class IObserver(metaclass=ABCMeta):
    def notify():
        pass


class Station(IObserver):
    name: str
    steps: List
    linked_barcode: str

    def __init__(self, observable, name):
        self.name = name
        observable.attach(self)
        self.linked_barcode = None

    def notify(self, *args, **kwargs):
        if self.linked_barcode == args[0]:
            print("Barcode {} was accepted at station {}".format(args[0], self.name))
        else:
            print("Barcode {} was rejected at station {}".format(args[0], self.name))
        print()
    

    def addStep(self, step):
        self.steps.append(step)

    def removeStep(self, step):
        self.steps.remove(step)

    def linkBarcode(self, barcode):
        self.linked_barcode = barcode
    
    def unlinkBarcode(self, barcode):
        self.linked_barcode = None


subject = Subject()
station_A = Station(subject, "A")
station_B = Station(subject, "B")

station_A.linkBarcode('AB321C8F7D')

subject.notifyObservers('AB321C8F7D')