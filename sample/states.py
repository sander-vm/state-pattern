from .state import State

class StopState(State):
    def handle1(self) -> None:
        print("StopState handle1")
        self.context.transition_to(StartState())

    def handle2(self) -> None:
        print("StopState handle2")

    def handle3(self) -> None:
        print("StopState handle3")

class StartState(State):
    def handle1(self) -> None:
        print("StartState handle1")

    def handle2(self) -> None:
        print("StartState handle2")
        self.context.transition_to(StopState())

    def handle3(self) -> None:
        print("StartState handle3")
        self.context.transition_to(PauseState())

class PauseState(State):
    def handle1(self) -> None:
        print("PauseState handle1")
        self.context.transition_to(StartState())

    def handle2(self) -> None:
        print("PauseState handle2")
        self.context.transition_to(StopState())

    def handle3(self) -> None:
        print("PauseState handle3")