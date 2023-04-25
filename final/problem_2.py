from abc import ABC, abstractmethod
from enum import Enum


# Notification Frequency Enum
class NotificationFrequency(Enum):
    ASAP = "ASAP"
    HOURLY = "Hourly"
    DAILY = "Daily"
    WEEKLY = "Weekly"


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
class Channel(Subject):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._videos = []

    def add_video(self, video):
        self._videos.append(video)
        self.notify()

    def get_latest_video(self):
        return self._videos[-1] if self._videos else None

    def get_name(self):
        return self._name


# Observer
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# ConcreteObserver
class Subscriber(Observer):
    def __init__(self, name, notification_frequency):
        self._name = name
        self._notification_frequency = notification_frequency

    def update(self, subject):
        if isinstance(subject, Channel):
            print(f"{self._name} received a notification: New video uploaded to {subject.get_name()} channel. "
                  f"Notification frequency: {self._notification_frequency.value}")

    def retrieve_video(self, channel):
        latest_video = channel.get_latest_video()
        if latest_video:
            print(f"{self._name} is watching the video: {latest_video}")
        else:
            print(f"No videos available on {channel.get_name()} channel")


# Main program
global_news = Channel("GlobalNews")
nba_inside = Channel("NBAInside")

maria = Subscriber("Maria", NotificationFrequency.ASAP)
john = Subscriber("John", NotificationFrequency.HOURLY)

global_news.attach(maria)
nba_inside.attach(john)
global_news.attach(john)

global_news.add_video("Breaking News: Earthquake in Japan")
nba_inside.add_video("NBA Highlights: Lakers vs. Warriors")

maria.retrieve_video(global_news)
john.retrieve_video(nba_inside)
john.retrieve_video(global_news)
