class Pila:

    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.elementos = []
        self.tope = 0

    def insertar(self, item):
        # Verificamos desbordamiento (Overflow)
        if self.tope >= self.capacidad:
            print(
                f"Error: Desbordamiento al intentar insertar '{item}'."
            )
            return False

        self.elementos.append(item)
        self.tope += 1

        print(
            f"Insertar('{item}') -> TOPE = {self.tope}"
        )
        return True

    def eliminar(self):
        # Verificamos subdesbordamiento (Underflow)
        if self.tope <= 0:
            print(
                "Error: Subdesbordamiento (Underflow). "
                "La pila está vacía, no se puede eliminar."
            )
            return None

        item = self.elementos.pop()
        self.tope -= 1

        print(f"Elemento extraído: '{item}'")
        return item

    def dibujar(self):
        # Dibujamos el estado actual de la pila
        print("Estado actual de la pila:")

        if not self.elementos:
            print("[ Pila vacía ]")
        else:
            for elemento in reversed(self.elementos):
                print("+-------+")
                print(f"|   {elemento}   |")
            print("+-------+")

        print(f"TOPE = {self.tope}")
        print(f"Elementos: {self.elementos}")
        print()


# --- Ejecución de las operaciones ---

mi_pila = Pila(capacidad=8)

print("--- ESTADO INICIAL ---")
mi_pila.dibujar()

# a. Insertar (PILA, X)
print("a. Insertar (PILA, X)")
mi_pila.insertar("X")
mi_pila.dibujar()

# b. Insertar (PILA, Y)
print("b. Insertar (PILA, Y)")
mi_pila.insertar("Y")
mi_pila.dibujar()

# c. Eliminar (PILA, Z)
print("c. Eliminar (PILA, Z)")
z = mi_pila.eliminar()
print(f"Z = {z}")
mi_pila.dibujar()

# d. Eliminar (PILA, T)
print("d. Eliminar (PILA, T)")
t = mi_pila.eliminar()
print(f"T = {t}")
mi_pila.dibujar()

# e. Eliminar (PILA, U)
print("e. Eliminar (PILA, U)")
u = mi_pila.eliminar()
print(f"U = {u}")
mi_pila.dibujar()

# f. Insertar (PILA, V)
print("f. Insertar (PILA, V)")
mi_pila.insertar("V")
mi_pila.dibujar()

# g. Insertar (PILA, W)
print("g. Insertar (PILA, W)")
mi_pila.insertar("W")
mi_pila.dibujar()

# h. Eliminar (PILA, p)
print("h. Eliminar (PILA, p)")
p = mi_pila.eliminar()
print(f"p = {p}")
mi_pila.dibujar()

# i. Insertar (PILA, R)
print("i. Insertar (PILA, R)")
mi_pila.insertar("R")
mi_pila.dibujar()

# --- Resultado final ---

print("--- RESULTADO FINAL ---")
print(f"Elementos finales en la pila: {mi_pila.elementos}")
print(f"Cantidad de elementos: {mi_pila.tope}")
print(f"Valor final del TOPE: {mi_pila.tope}")