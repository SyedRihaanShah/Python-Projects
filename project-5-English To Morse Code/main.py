English_to_MorseCode = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " " : "/"
}

InputStr = input("Enter the string you want to convert into morse code: ").lower()

Repetations = len(InputStr)
output = ""
try:    
    for rep in range(0,Repetations):
         if InputStr[rep] in English_to_MorseCode:
            output = output + English_to_MorseCode.get(InputStr[rep])
         else:
             raise ValueError(f'invalid character : {InputStr[rep]}')
    print(f"The convereted string is {output}")

except ValueError as e :
    print(e)
