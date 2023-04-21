from abc import ABC, abstractmethod


# Subject
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


# ConcreteSubject
class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_pressure(self):
        return self._pressure


# Observer
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# ConcreteObserver
class WeatherDisplay(Observer):
    def __init__(self, weather_data):
        self._weather_data = weather_data
        self._weather_data.attach(self)

    def update(self, subject):
        if subject == self._weather_data:
            print(f"Temperature: {subject.get_temperature()}°C, Humidity: {subject.get_humidity()}%, Pressure: {subject.get_pressure()} hPa")


# Client
weather_data = WeatherData()
weather_display = WeatherDisplay(weather_data)

weather_data.set_measurements(25, 65, 1013)
weather_data.set_measurements(27, 60, 1010)
