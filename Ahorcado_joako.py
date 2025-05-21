# utilice como base el codigo de belen
#importamos el modulo random
import random

# Lista de palabras posibles
palabras = ["python", "computadora", "programa", "teclado", "monitor", "ahorcado", "juego", "letras"]

# Función para mostrar la palabra oculta con guiones
def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Función principal del juego
def jugar():
    palabra = random.choice(palabras)
    letras_adivinadas = []
    letras_incorrectas = []
    vidas = 6

    print("¡Bienvenido al juego Ahorcado! ¡Adivina la Palabra!")
    print("Tienes que adivinar la palabra letra por letra.")
    #letras incorrectas
    while True:
        print("\nPalabra:", mostrar_palabra(palabra, letras_adivinadas))
        print("Vidas restantes:", vidas)
        print("Letras incorrectas:", ", ".join(letras_incorrectas))

        intento = input("Ingresa una letra: ").lower()

    # Validar entrada
        if not intento.isalpha() or len(intento) != 1:
            print("Por favor, ingresa solo UNA letra válida.")
            continue
    # Entrada repetida   
        if intento in letras_adivinadas or intento in letras_incorrectas:
            print("Ya intentaste con esa letra. Probá otra.")
            continue
    # Letra correcta 
        if intento in palabra:
            letras_adivinadas.append(intento)
            print("¡Bien! La letra está en la palabra.")
    # cantidad  de vidas
        else:
            letras_incorrectas.append(intento)
            vidas -= 1
            print("La letra no está en la palabra.")
    #fin del juego
        if all(letra in letras_adivinadas for letra in palabra):
            print("\n¡Felicidades! Adivinaste la palabra:", palabra)
            break

        if vidas == 0:
            print("\n¡Te quedaste sin vidas! La palabra era:", palabra)
            break

if __name__ == "__main__":
    jugar()
