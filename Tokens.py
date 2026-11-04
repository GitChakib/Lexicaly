

#NEEDED FOR MATCHING (instead of writing "L/N" just write letters + (same as or) numbers)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"



class Token:

    def __init__(self, name, string):
        self.name = name
        self.string = string

    def match_token(self, text, pos):
        start_pos = pos

        for chars, repeats in self.string:
            if not repeats:
                if pos < len(text) and text[pos] in chars:
                    pos += 1
                else:
                    return None
            else:
                while pos < len(text) and text[pos] in chars:
                    pos += 1
                    
        if pos == start_pos:
            return None
        
        return self.name

#defining our tokens

#every token is a tuple of a name and a list of characters and whether they can be repeated

IF = Token("IF", [("i", False), ("f", False)]) 
ID = Token("ID", [(letters, True), (letters + numbers, True)])
ELSE = Token("ELSE", [("e", False), ("l", False), ("s", False), ("e", False)])

#functtion to read string and match it with the token
       
if __name__ == "__main__":

    for text in ["if", "chakib", "and", "abc123", "print","else", "return"]:

        print(f"{text} {IF.match_token(text, 0) or ELSE.match_token(text, 0) or ID.match_token(text, 0)}")

#CURRENT ERROR IS IN MATCH_TOKEN FUNCTION