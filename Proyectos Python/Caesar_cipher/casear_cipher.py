alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

direccion = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shiftNumber = int(input("Type the shift number:\n"))



def encrpyt(shift,texto):
    cipherText = ""
    for letter in texto:
        if letter == " ":
            cipherText += " "
        else:
            position = alfabeto.index(letter)
            newPosition = position + shift
            newLetter = alfabeto[newPosition]
            cipherText += newLetter
    print(f"{cipherText}")


def decrypt(shift,texto):
    decryptText = ""
    for letter in texto:
        if letter == " ":
            decryptText += " "
        else:
            position = alfabeto.index(letter)
            newPosition = position - shift
            newLetter = alfabeto[newPosition]
            decryptText += newLetter
    print(f"{decryptText}")


if direccion == "encode":
    encrpyt(shift = shiftNumber,texto = text)
elif direccion == "decode":
    decrypt(shift = shiftNumber,texto = text)
else:
    print("Thats not what I want")

