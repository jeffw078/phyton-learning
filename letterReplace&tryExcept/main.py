#LEARNING LETTER REPLACEMENT
#LEARNING PYTHON EXCEPT TO AVOID ERRORS

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Digite uma frase: ")))

try:
    number = int(input("Digite um número: "))
    print(number)
except:
    print("Bixo Burro")

