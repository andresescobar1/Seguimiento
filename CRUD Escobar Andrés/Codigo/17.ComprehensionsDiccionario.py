import os

# Crear el diccionario que asocia cada número con su cuadrado
cuadrados = {i: i**2 for i in range(1, 101)}

def mostrar_menu():
    print("Menú:")
    print("1. Ver el cuadrado de un número")
    print("2. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == '1':
        try:
            numero = int(input("Ingresa un número entre 1 y 100: "))
            if 1 <= numero <= 100:
                print(f"El cuadrado de {numero} es {cuadrados[numero]}.")
            else:
                print("Número fuera de rango. Debe estar entre 1 y 100.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    elif opcion == '2':
        # Limpiar la pantalla antes de salir
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Intenta nuevamente.")

