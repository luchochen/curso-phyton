# =========================
# EJERCICIO: MAXIKIOSCO
# =========================

# 1) Diccionario del negocio (llave y valor)
negocio = {
    "Nombre": "Maxikiosco 24/7",
    "Servicios": "Venta de bebidas, snacks, recargas, cigarrillos",
    "Dirección": "Av. Principal 123",
    "Horario": "365 días - 24 horas",
    "Contacto": "+54 341 000-0000"
}

# 2) Lista anidada (lista de tuplas) con productos y stock
# (Teclados, Mouse, Monitores... eran ejemplo; acá lo adaptamos a kiosco)
productos = [
    ("Gaseosa", 1500, 12),
    ("Galletitas", 2500, 20),
    ("Carbón", 3500, 0)  # <- al menos un artículo con stock 0
]

# 3) Tupla de empleados (podés cambiar nombres)
empleados = ("Ema", "Chelo", "Emi", "Jesús")

# =========================
# FUNCIONES
# =========================
def mostrar_bienvenida():
    print("\n" + "=" * 40)
    print("Bienvenido al Maxikiosco más completo de la ciudad")
    print("Abrimos los 365 días - 24 horas")
    print("=" * 40)

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1 - Información del negocio")
    print("2 - Nuestros productos")
    print("3 - Empleados")
    print("4 - Salir")

def opcion_info_negocio():
    print("\n--- Información del negocio ---")
    for clave, valor in negocio.items():
        print(f"{clave}: {valor}")

def opcion_productos():
    print("\n--- Nuestros productos ---")
    for nombre, precio, stock in productos:
        if stock == 0:
            print(f"{nombre} - ${precio} -> Sin Stock (mañana llega!)")
        else:
            print(f"{nombre} - ${precio} -> Stock: {stock}")

def opcion_empleados():
    print("\n--- Empleados ---")
    for i, emp in enumerate(empleados, start=1):
        print(f"{i}. {emp}")

# =========================
# PROGRAMA PRINCIPAL (loop)
# =========================
mostrar_bienvenida()

while True:
    mostrar_menu()
    opcion = input("Elegí una opción (1-4): ").strip()

    if opcion == "1":
        opcion_info_negocio()
    elif opcion == "2":
        opcion_productos()
    elif opcion == "3":
        opcion_empleados()
    elif opcion == "4":
        print("\nGracias por visitar el Maxikiosco. ¡Hasta luego!")
        break
    else:
        print("\nOpción inválida. Elegí 1, 2, 3 o 4.")
