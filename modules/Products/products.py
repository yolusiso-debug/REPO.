import random

numero_secreto = random.randint(1, 20)
intentos = 0

print("🎯 ¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 20. ¿Puedes adivinarlo?")

while True:
    intento = int(input("Introduce tu número: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("❌ Demasiado bajo. ¡Intenta otra vez!")
    elif intento > numero_secreto:
        print("❌ Demasiado alto. ¡Intenta otra vez!")
    else:
        print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
