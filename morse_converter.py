morse_dict = {
    'a': '*-',
    'b': '-***',
    'c': '-*-*',
    'd': '-**',
    'e': '*',
    'f': '**-*',
    'g': '--*',
    'h': '****',
    'i': '**',
    'j': '*---',
    'k': '-*-',
    'l': '*-**',
    'm': '--',
    'n': '-*',
    'o': '---',
    'p': '*--*',
    'q': '--*-',
    'r': '*-*',
    's': '***',
    't': '-',
    'u': '**-',
    'v': '***-',
    'w': '*--',
    'x': '-**-',
    'y': '-*--',
    'z': '--**',
    ' ': '***',
    '0': '-----',
    '1': '*----',
    '2': '**---',
    '3': '***--',
    '4': '****-',
    '5': '*****',
    '6': '-****',
    '7': '--***',
    '8': '---**',
    '9': '----*',
    '.': '*-*-*-',
    ',': '--**--',
    '?': '**--**',
    "'": '*----*',
    '!': '-*-*--',
    '/': '-**-*',
    '(': '-*--*',
    ')': '-*--*-',
    '&': '*-***',
    ':': '---***',
    ';': '-*-*-*',
    '=': '-***-',
    '+': '*-*-*',
    '-': '-****-',
    '_': '**--*-',
    '"': '*-**-*',
    '$': '****-**-',
    '@': '*--*-*',
}

class MorseConverter:
    def __init__(self):
        self.dict = morse_dict
        self.char_list = []
        self.morse_list = []
        self.morse_string = ''

    def string_to_list(self, string):
        """Converts a string into a list of individual characters. Resets morse_string to an empty string"""
        self.morse_string = ""
        self.char_list = []
        self.char_list[:0] = string
        return self.char_list

    def to_morse(self, char_list):
        """Transforms a list of alphabet characters to morse code"""
        for char in char_list:
            try:
                morse = self.dict[char]
                self.morse_list.append(morse)

            except KeyError:
                pass
        print(self.morse_list)
        return self.morse_list

    def to_string (self):
        for _ in self.morse_list:
            self.morse_string += _
            self.morse_string += ' '
            self.char_list = []
            self.morse_list = []
        return self.morse_string


