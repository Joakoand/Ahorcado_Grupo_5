#importamos el modulo random
import random

#creamos una lista con palabras
palabras = ["python", "computadora", "programa", "teclado", "monitor"]

#definimos las variables a utilizar
palabra = random.choice(palabras)
letras_adivinadas = []
vidas = 6
#mensajes a mostrar
print("¡Bienvenido al juego 'Adivina la palabra'!")
print("Tienes", vidas, "vidas.")
print("Palabra:", "_ " * len(palabra))

while vidas > 0:
    letra = input("Ingresa una letra: ").lower()

    # Validar entrada
    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, ingresa una sola letra válida.")
        continue

    if letra in letras_adivinadas:
        print("Ya intentaste con esa letra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra:
        print("¡Bien! La letra está en la palabra.")
    else:
        vidas -= 1
        print("Incorrecto. Te quedan", vidas, "vidas.")

   
    progreso = ""
    for l in palabra:
        if l in letras_adivinadas:
            progreso += l + " "
        else:
            progreso += "_ "

    print("Palabra:", progreso)

#fin del juego
    if all(l in letras_adivinadas for l in palabra):
        print("¡Felicidades! Adivinaste la palabra:", palabra)
        break
else:
    print("¡Perdiste! La palabra era:", palabra)