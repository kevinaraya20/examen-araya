import random
# Lista de nombres de trabajadores
trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

# Lista de sueldos inicialmente vacía
sueldos = []

# Función para asignar sueldos aleatorios a los empleados
def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(len(trabajadores))]
    print("Sueldos asignados aleatoriamente.")


# Función para clasificar los sueldos
def clasificar_sueldos():
    if not sueldos:
        print("Aún no se han asignado sueldos.")
        return
    
    sueldos_ordenados = sorted(sueldos)
    print("Sueldos clasificados de menor a mayor:")
    for index, sueldo in enumerate(sueldos_ordenados, start=1):
        print(f"Empleado {index}: {sueldo}")



# Función para mostrar estadísticas de sueldos
def ver_estadisticas():
    if not sueldos:
        print("Aún no se han asignado sueldos.")
        return
    
    total_empleados = len(sueldos)
    total_sueldos = sum(sueldos)
    sueldo_promedio = total_sueldos / total_empleados
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)

    print("Estadísticas de sueldos:")
    print(f"Número total de empleados: {total_empleados}")
    print(f"Sueldo promedio: {sueldo_promedio:.2f}")
    print(f"Sueldo máximo: {sueldo_maximo}")
    print(f"Sueldo mínimo: {sueldo_minimo}")
    

# Función para generar un reporte de sueldos
def generar_reporte():
    if not sueldos:
        print("Aún no se han asignado sueldos.")
        return
    
    print("Reporte de sueldos:")
    for index, trabajador in enumerate(trabajadores):
        print(f"{trabajador}: {sueldos[index]}")

# Función principal que maneja el menú
def main():
    while True:
        print("\Menú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            asignar_sueldos_aleatorios()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            print("Saliendo del programa... has salido con exito :) ")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
 main()
