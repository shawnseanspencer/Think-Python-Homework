#Strips a text file of all punctuation and makes all letters lowercase.

import string as str

def textstrip(text):
    fin = open(text)
    final = ""
    for line in fin:
        phrase = line.strip()

        for char in phrase:
            if char in str.punctuation or char in str.whitespace:
                None
            elif char == char.upper():
                final += char.lower()
            else:
                final += char

    return final
    
                

print(textstrip("shakespeare.txt"))
