import random

contador = 0
vidas = 4
textoLargo = "__________"
textoMediano = "______"
textoCorto = "____"

def StartGame():
    
    words = ["python", "javascript", "ruby", "java", "rust", "dart"]
    numeroRandom = random.randint(0,6)
    selectedWord = words[numeroRandom - 1]
    largoDeLaPalabra = len(selectedWord)
    if len(selectedWord) == 4:
        print(f"Vidas: {vidas}")
        print(f"{textoCorto}")
    elif len(selectedWord) == 6:
        print(f"Vidas: {vidas}")
        print(f"{textoMediano}")
    elif len(selectedWord) == 10:
        print(f"Vidas: {vidas}")
        print(f"{textoLargo}")
    
    letraElegida = input("Letra que elegís: ")
    lst = []
    for pos,char in enumerate(selectedWord):
        if(char == letraElegida):
            lst.append(pos)
    print(lst)

    


    

StartGame()
