class State:

    def __init__(self, name, transitions):

        self.name = name
        self.transitions = []

    def add_transition(self, chars, next_state):

        self.transitions.append((chars, next_state))


q0 = State("q0", [])
q1 = State("q1", [])