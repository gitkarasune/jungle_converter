def get_language():
    return input("Input language (jungle/english): ").strip().lower()

def translation(words, language):
    converter = {
        "a": "1", "e": "2", "i": "3", "o": "4", "u": "5", "A": "1", "E": "2", "I": "3", "O": "4", "U": "5",
        'q': "qa", "w": "wa", "r": 'ra', 't': "ta", "y": "ya", "p": "pa", 's': "sa", "d": "da", "f": "fa",
        "g": "ga", "h": "ha", "j": "ja", "k": "ka", 'l': 'la', "z": "za", "x": "xa", "c": "ca", "v": "va",
        "b": "ba", "n": "na", "m": "ma", "Q": "Qa", "W": "Wa", "R": "Ra", "T": "Ta", "Y": "Ya", "P": 'Pa',
        "S": "Sa", "D": "Da", "F": "Fa", "G": "Ga", "H": "Ha", "J": "Ja", "K": "Ka", "L": "La", "Z": "Za",
        "X": "Xa", "C": "Ca", "V": "Va", "B": "Ba", "N": "Na", "M": "Ma"
    }
    translator = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}

    output = ""
    if language == "jungle":
        for word in words:
            if word in ["a", "A"]:
                word = ""
            output += translator.get(word, word)
    elif language == "english":
        for word in words:
            output += converter.get(word, word)
    return output

def main():
    words = input('Input words: ')
    language = get_language()
    translated_words = translation(words, language)
    print("Translated words:", translated_words)

if __name__ == "__main__":
    main()