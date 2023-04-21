from abc import ABC, abstractmethod


# Subject Interface
class ISubject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


# RealSubject
class RealSubject(ISubject):
    def request(self) -> None:
        print("RealSubject: Handling request.")


# Proxy
class Proxy(ISubject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def _check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def _log_access(self) -> None:
        print("Proxy: Logging the time of request.")

    def request(self) -> None:
        if self._check_access():
            self._real_subject.request()
            self._log_access()


# Client code
def client_code(subject: ISubject) -> None:
    subject.request()


print("Client: Executing the client code with a real subject:")
real_subject = RealSubject()
client_code(real_subject)

print("\nClient: Executing the same client code with a proxy:")
proxy = Proxy(real_subject)
client_code(proxy)
