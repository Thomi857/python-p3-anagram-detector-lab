class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    
    @word.setter  
    def word(self, value):
        if isinstance(value, str):
            self._word = value.lower()
        else:
            raise ValueError("Word must be a string")

    def match(self, word_list):
            matches = []
            for canditate in word_list:
                if sorted(canditate.lower()) == sorted(self.word.lower()) and canditate.lower() != self.word.lower():
                    matches.append(canditate)
            return matches
            
                
        
        

