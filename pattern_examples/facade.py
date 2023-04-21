# Subsystem classes (complex system components)
class SubsystemA:
    def operation_a(self):
        return "Subsystem A: Performing operation A"


class SubsystemB:
    def operation_b(self):
        return "Subsystem B: Performing operation B"


class SubsystemC:
    def operation_c(self):
        return "Subsystem C: Performing operation C"


class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def perform_operation(self):
        result = []

        result.append(self._subsystem_a.operation_a())
        result.append(self._subsystem_b.operation_b())
        result.append(self._subsystem_c.operation_c())

        return "\n".join(result)


facade = Facade()
print(facade.perform_operation(), end="")
