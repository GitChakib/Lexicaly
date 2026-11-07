#every state is an object that has a name and a list of possible transitions and if it can be repeated

class State:

    def __init__(self, name, transitions, is_repeated=False):

        self.name = name
        self.is_repeated = False
        self.transitions = []

    def add_transition(self, char, next_state):

        self.transitions.append((char, next_state))


q0 = State("q0", [])
q1 = State("q1", [])

# need to fix this error q0's transitions: [('a', <__main__.State object at 0x000001D4F4F48410>)]


q0.add_transition('a', q1)

print(f"{q0.name}'s transitions: {q0.transitions}")