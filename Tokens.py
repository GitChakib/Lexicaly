

#NEEDED FOR MATCHING (instead of writing "L/N" just write letters + (same as or) numbers)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"


class Token:
    def __init__(self, name, string):
        self.name = name
        self.string = string


#defining our tokens

IF = Token("IF", [("i", False), ("f", False)]) #every token is a tuple of a name and a list of characters and whether they can be repeated

#functtion to read string and match it with the token

def match_token(self, text, pos):

    start_pos = pos
    
    for chars, repeats in self.string:
       
       if not repeats:
         
         if pos < len(text) and text[chars]:

            pos += 1

         else: return "error"

       else:
          
          while pos < len(text) and text[chars]:
             
             pos += 1

          return text[start_pos:pos]
