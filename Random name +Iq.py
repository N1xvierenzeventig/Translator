
def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "QEIOqiuo":
            translation = translation + "a"
        else:
            translation = translation + letter
    return translation

print(translator(input("Write the word or phrase which you want to be translated: ")))






