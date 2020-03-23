from abc import ABC, abstractmethod

class Context(ABC):
    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def start(self):
        self._state.handle1()

    def stop(self):
        self._state.handle2()
            
    def pause(self):
        self._state.handle3()    
