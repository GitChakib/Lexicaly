

#NEEDED FOR MATCHING (instead of writing "L/N" just write letters + (same as or) numbers)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

class Token:
    def __init__(self, name, string):
        self.name = name
        self.string = string

#functtion to read string and match it with the token

def match_token(self, string, pos):
    start_pos = pos
