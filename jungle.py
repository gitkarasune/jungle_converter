words = input("input language: ")
language = ""
converter = {"a": "1",
"e": "2", "i": "3", "o": "4",
"u": "5", "A": "1", "E": "2",
"I": "3", "O": "4", "U": "5",
'q': "qa", "w": "wa", "r": 'ra',
't': "ta", "y": "ya", "p": "pa",
"s": "sa", "d": "da", "f": "fa",
"g": "ga", "h": "ha", "j": "ja",
"k": "ka", 'l': 'la', "z": "za",
"x": "xa", "c": "ca", "v": "va",
"b": "ba", "n": "na", "m": "ma",
"Q": "Qa", "W": "Wa", "R": "Ra",
"T": "Ta", "Y": "Ya", "P": 'Pa',
"S": "Sa", "D": "Da", "F": "Fa",
"G": "Ga", "H": "Ha", "J": "Ja",
"K": "Ka", "L": "La", "Z": "Za",
"X": "Xa", "C": "Ca", "V": "Va",
"B": "Ba", "N": "Na", "M": "Ma"}
translator = {"1": "a", "2": "e",
"3": "i", "4": "o", "5": "u"}


def translation():
    output = ""
    if language.lower() == "jungle":
        for word in words:
            if word == "a":
                word = ""
            elif word == "A":
                word = ""
            output += translator.get(word, word)
    elif language.lower() == "english":
        for word in words:
            output += converter.get(word, word)
    return output

for word in words:
    if word in "12345":
        language = "jungle"
    else:
        language = "english"
print(translation())
