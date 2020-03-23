from sample.context import Context
from sample.states import StopState

if __name__ == '__main__':
    print("starting main")
    context = Context(StopState())
    context.start()
    context.pause()
    context.stop()
    context.start()