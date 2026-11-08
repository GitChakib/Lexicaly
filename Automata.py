#every state is an object that has a name and a list of possible transitions and if it can be repeated
from Tokens import IF, ID, ELSE


class State:

    def __init__(self, name, transitions, is_repeated = False, is_final = False, is_start = False):

        self.name = name
        self.is_repeated = is_repeated
        self.transitions = transitions
        self.is_final = is_final
        self.is_start = is_start

    def add_transition(self, char, next_state):

        self.transitions.append((char, next_state))

    def __repr__(self):

        return self.name

def state_maker(token):

        start = State("q0", [], is_start = True)
        currentState = start
        stateIndex = 1

        for chars, repeats in token.string: 

            if repeats:

                currentState.add_transition(chars, currentState)
                currentState.is_repeated = True

            else:

                nextState = State(f"q{stateIndex}", [])
                currentState.add_transition(chars, nextState)
                currentState = nextState
                stateIndex += 1

        currentState.is_final = True
        currentTokenName = token.name

        return start

def printAutomata(start):

    visitedState = []
    toVisit = [start]

    while toVisit:

        currentState = toVisit.pop(0)

        if currentState in visitedState:
            continue
        visitedState.append(State)

        for chars, nextState in currentState.transitions:

            print(f"{currentState.name} --{chars}--> {nextState.name}")

            toVisit.append(nextState)


if __name__ == "__main__":
    for token in [IF, ID, ELSE]:
        print(f"--- {token.name} ---")
        printAutomata(state_maker(token))