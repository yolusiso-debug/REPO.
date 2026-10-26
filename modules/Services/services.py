import time
import os

print("⏰ Reloj en tiempo real (Presiona Ctrl+C para salir):")

try:
    while True:
        # Obtiene la hora actual formateada
        hora_actual = time.strftime("%H:%M:%S")
        
        # Imprime la hora sobreescribiendo la línea anterior
        print(f"\rHora actual: {hora_actual}", end="")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("\n👋 ¡Reloj detenido!")
