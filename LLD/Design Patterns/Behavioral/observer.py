"""
Use Case:
when we have something like a pair of observer and observable. 
For example: In amazon we can subscribe to an item if it is out of stock.
so we are the observer, the item is the observable

Code Summary:
We have observable class with some methods like
add: to add an observer
remove: to remove an observer
notify: call the observers
set_data: update the data, and then call notify
get_data: gets data, used by the observer

We have observer class with methods like
update: this is called by the observable to notify
"""

# Sample use case: Weather service which notifies the temperatures across multiple devices

from abc import ABC, abstractmethod

class WeatherServiceInterface(ABC):
    @abstractmethod
    def add(self, observer_obj):
        pass

    @abstractmethod
    def remove(self, observer_obj):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def set_data(self, temp):
        pass

    def get_data(self):
        return self.temp

class WeatherService(WeatherServiceInterface):
    def __init__(self):
        self.temp = 22
        self.observers = []

    def add(self, observer_obj):
        self.observers.append(observer_obj)
    
    def remove(self, observer_obj):
        # remove from observers list
        pass

    def notify(self):
        for observer in self.observers:
            observer.update()

    def set_data(self, new_temp):
        self.temp = new_temp
        self.notify()

class DisplayInterface(ABC):
    @abstractmethod
    def update(self):
        pass

class TVDisplay(DisplayInterface):
    def __init__(self, weather_service_obj):
        self.weather_service_obj = weather_service_obj

    def update(self):
        print("Printing from TV, new temp = ", self.weather_service_obj.get_data())

class MobileDisplay(DisplayInterface):
    def __init__(self, weather_service_obj):
        self.weather_service_obj = weather_service_obj

    def update(self):
        print("Printing from Mobile, new temp = ", self.weather_service_obj.get_data())

if __name__ == "__main__":
    weather_service_obj = WeatherService()
    print("Initial temperature = ", weather_service_obj.get_data())
    tv_display = TVDisplay(weather_service_obj)
    mobile_display = MobileDisplay(weather_service_obj)

    weather_service_obj.add(tv_display)
    weather_service_obj.set_data(26)

    weather_service_obj.add(mobile_display)
    weather_service_obj.set_data(28)