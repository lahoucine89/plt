class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"  
        
        words = self.phrase.split()
        translated_words = [self._translate_word(word) for word in words]
        return ' '.join(translated_words)
    
    def _translate_word(self, word: str) -> str:
       
        punctuation = ''
        if word[-1] in ".,;:!?()":
            punctuation = word[-1]
            word = word[:-1]

       
        if not word.isupper() and not word.istitle() and not word.islower():
            raise PigLatinError("Words must be either lowercase, uppercase, or title-case")

       
        if word[0] in "aeiouAEIOU":
            if word[-1] == 'y':
                translation = word + "nay"
            elif word[-1] in "aeiouAEIOU":
                translation = word + "yay"
            else:
                translation = word + "ay"
        
       
        else:
            first_vowel_index = next((i for i, letter in enumerate(word) if letter in "aeiouAEIOU"), len(word))
            translation = word[first_vowel_index:] + word[:first_vowel_index] + "ay"
        
        return translation + punctuation
