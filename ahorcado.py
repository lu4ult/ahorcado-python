import requests, os

url = 'https://palabras-aleatorias-public-api.herokuapp.com/random'
respuesta = requests.get(url)

palabra = respuesta.json()['body']['Word']
definicion = respuesta.json()['body']['DefinitionMD']

definicion = definicion.replace(palabra,'*' * len(palabra))  #aveces la definición de la palabra incluye la palabra en sí, por eso la reemplazamos por asteriscos para evitar verla
definicion = definicion[:100]                                  #aveces la descripción trae un montón de otra información como sinónimos o códigos HTML, asi que limitamos la respuesta
    
lista_letras = []
vidas = 3

print(f"Juego del ahorcado.\nPalabras clave:\n\t*rendirse\n\t*salir\n\t*pista\n")
while(vidas):
    print(f"\nVidas restantes: {vidas}\nLetras usadas:")
    for i in lista_letras:                              #Primero publicamos las letras que hemos ingreado, hayan sido acertadas o perdedoras
            print(i, end="-")
    print("\n")

    letras_acertadas = 0
    for i in palabra:                                   #Recorremos cada letra dentro de la palabra random, 
        if i in lista_letras:                           #si esa letra ya se seleccionó (se encuentra en la lista de letras) la pubicamos, sino publica un "_"
            letras_acertadas += 1
            print(i, end=" ")
        else:
            print("_", end=" ")
    print("\n\n")
    
    if letras_acertadas == len(palabra):
        print("\n\n\t\tGANASTE!!")
        input("Presione cualquier tecla para salir")
        sys.exit()
            
    letra = input("Ingrese letra: ").lower()
    os.system('cls')                                    #Para borrar la pantalla en DOS
    if letra == "pista":
        print(f"Pista:\n{definicion}\n\n")
    if letra == "salir":
        break
    if letra == "rendirse":
        vidas = 0                                       #Colocamos las vidas en 0 ya que mas abajo se imprime el mensaje de "Perdiste"
        
    if not letra in lista_letras and len(letra) == 1:   #Agregamos la letra a la lista de letras ingresadas y si no está en la palabra random descontamos una vida  
        lista_letras.append(letra)
        lista_letras.sort()        
        if not letra in palabra:
            vidas -= 1
    if not vidas:
        print(f"PERDISTE!\nLa palabra era {palabra}")
        input("Presione cualquier tecla para salir")                  
