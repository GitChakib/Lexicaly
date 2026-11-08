#every state is an object that has a name and a list of possible transitions and if it can be repeated

from Tokens import IF, ID, ELSE
from Tokens import letters, numbers


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


#function that takes token and builds states from it

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

        return start

def printAutomata(start):

#function for taking the start of the automata and traverses with each iteration printing the transitions of the next state

    visitedState = []
    toVisit = [start]

    while toVisit:

        currentState = toVisit.pop(0)

        if currentState in visitedState:
            continue
        visitedState.append(currentState)

        for chars, nextState in currentState.transitions:

            if chars == letters :

                print (f"{currentState.name} --Letters--> {nextState.name}") #only for simplyfying letters instead of mashup of letters

            elif chars == letters + numbers:

                print (f"{currentState.name} --Letters + Numbers--> {nextState.name}") #only for simplyfying letters instead of mashup of letters and numbers

            else:

              print(f"{currentState.name} --{chars}--> {nextState.name}") #only for simplyfying letters instead of mashup of letters and numbers

            toVisit.append(nextState)

            if currentState.is_final == True:

                print (f"{currentState.name} Is Final! --> {token.name}")


if __name__ == "__main__":
    for token in [IF, ELSE, ID]:
        print(f"--- {token.name} ---")
        printAutomata(state_maker(token))