

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

         else: return None

       else:
          
          while pos < len(text) and text[pos] in chars:
             
             pos += 1

          return text[start_pos:pos]


#defining our tokens

#every token is a tuple of a name and a list of characters and whether they can be repeated

IF = Token("IF", [("i", False), ("f", False)]) 
ID = Token("ID", [(letters, True), (numbers, True)])

#functtion to read string and match it with the token
       
if __name__ == "__main__":

     for text in ["if", "iffy", "count2", "2abc"]:
        print(f"text {text!r:9} IF -> {IF.match_token(text, 0)!r:6} ID -> {ID.match_token(text, 0)!r}")
