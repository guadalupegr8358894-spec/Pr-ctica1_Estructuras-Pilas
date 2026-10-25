1. Estados de la pila paso a paso

Condiciones iniciales

- Capacidad máxima: 8 elementos.

- Pila vacía: TOPE = 0.

- Regla LIFO (Last In, First Out): el último elemento que entra es el primero que sale.

- Los elementos se muestran desde el fondo hasta el tope. En los dibujos verticales, el tope está arriba.

Estado inicial

- Pila: [ ]

- TOPE = 0

a. Insertar (PILA, X)

Se inserta el elemento X. El TOPE pasa de 0 a 1.

- Pila: [X]

- TOPE = 1

+-------+
|   X   |  <-- TOPE = 1
+-------+

b. Insertar (PILA, Y)

Se inserta Y encima de X. El TOPE pasa de 1 a 2.

- Pila: [X, Y]

- TOPE = 2

+-------+
|   Y   |  <-- TOPE = 2
+-------+
|   X   |  <-- Fondo de la pila
+-------+

c. Eliminar (PILA, Z)

Se extrae Y, que está en el tope, y se almacena en la variable Z. El TOPE pasa de 2 a 1.

- Pila: [X]

- TOPE = 1

+-------+
|   X   |  <-- TOPE = 1
+-------+

Elemento eliminado: Y
Z = Y

d. Eliminar (PILA, T)

Se extrae X y se almacena en la variable T. La pila queda vacía y el TOPE pasa de 1 a 0.

- Pila: [ ]

- TOPE = 0

[ Pila vacía ]

TOPE = 0

Elemento eliminado: X
T = X

e. Eliminar (PILA, U)

Se intenta eliminar un elemento, pero la pila está vacía.

- Pila: [ ]

- TOPE = 0

[ Pila vacía ]

TOPE = 0

ERROR: Subdesbordamiento (Underflow)

Explicación: ocurre un subdesbordamiento (Underflow) porque se intenta extraer un elemento de una pila vacía. La operación no se ejecuta y la pila permanece sin elementos.

f. Insertar (PILA, V)

Se inserta V. El TOPE pasa de 0 a 1.

- Pila: [V]

- TOPE = 1

+-------+
|   V   |  <-- TOPE = 1
+-------+

g. Insertar (PILA, W)

Se inserta W encima de V. El TOPE pasa de 1 a 2.

- Pila: [V, W]

- TOPE = 2

+-------+
|   W   |  <-- TOPE = 2
+-------+
|   V   |
+-------+

h. Eliminar (PILA, p)

Se extrae W, que está en el tope, y se almacena en la variable p. El TOPE pasa de 2 a 1.

- Pila: [V]

- TOPE = 1

+-------+
|   V   |  <-- TOPE = 1
+-------+

Elemento eliminado: W
p = W

i. Insertar (PILA, R)

Se inserta R encima de V. El TOPE pasa de 1 a 2.

- Pila: [V, R]

- TOPE = 2

+-------+
|   R   |  <-- TOPE = 2
+-------+
|   V   |  <-- Fondo de la pila
+-------+

2. Preguntas del problema

¿Con cuántos elementos quedó la pila?

La pila quedó con 2 elementos: V y R. El puntero TOPE = 2. El elemento R se encuentra en el tope y V en el fondo de la pila.

¿Hubo algún caso de error (desbordamiento o subdesbordamiento)? Si ocurrió algún error, explícalo.

Sí, ocurrió un error de subdesbordamiento (Underflow) en el inciso e, Eliminar (PILA, U).

El subdesbordamiento sucede cuando se intenta eliminar un elemento de una pila vacía (TOPE = 0). Como no hay ningún elemento almacenado, no es posible extraer uno y la operación no se ejecuta.

No ocurrió desbordamiento (Overflow), porque nunca se superó la capacidad máxima de 8 elementos.

3. Código en Python que resuelve el problema

Este programa implementa una clase llamada Pila con capacidad máxima de 8 elementos. Ejecuta las operaciones indicadas, muestra los cambios de la pila y controla los errores de desbordamiento y subdesbordamiento.

Copia todo el código siguiente en un mismo archivo de Python, por ejemplo, pila.py. No omitas las líneas que están después de la clase.

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
        f"Insertar('{item}') -> TOPE = {self.tope} "    
        f"| Pila: {self.elementos}"    
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

    print(    
        f"Eliminar() -> Elemento extraído: '{item}' "    
        f"| TOPE = {self.tope} | Pila: {self.elementos}"    
    )    
    return item

--- Ejecución de la secuencia de operaciones ---

print("--- ESTADO INICIAL ---")

mi_pila = Pila(capacidad=8)

print(f"TOPE = {mi_pila.tope} | Pila: {mi_pila.elementos}")
print()

print("--- EJECUCIÓN DE LAS OPERACIONES ---")

a. Insertar (PILA, X)

print("\na. Insertar (PILA, X)")
mi_pila.insertar("X")

b. Insertar (PILA, Y)

print("\nb. Insertar (PILA, Y)")
mi_pila.insertar("Y")

c. Eliminar (PILA, Z)

print("\nc. Eliminar (PILA, Z)")
z = mi_pila.eliminar()

d. Eliminar (PILA, T)

print("\nd. Eliminar (PILA, T)")
t = mi_pila.eliminar()

e. Eliminar (PILA, U)

print("\ne. Eliminar (PILA, U)")
u = mi_pila.eliminar()

f. Insertar (PILA, V)

print("\nf. Insertar (PILA, V)")
mi_pila.insertar("V")

g. Insertar (PILA, W)

print("\ng. Insertar (PILA, W)")
mi_pila.insertar("W")

h. Eliminar (PILA, p)

print("\nh. Eliminar (PILA, p)")
p = mi_pila.eliminar()

i. Insertar (PILA, R)

print("\ni. Insertar (PILA, R)")
mi_pila.insertar("R")

--- Resultado final ---

print("\n--- RESULTADO FINAL ---")
print(f"Elementos finales en la pila: {mi_pila.elementos}")
print(f"Cantidad de elementos: {mi_pila.tope}")
print(f"Valor final del TOPE: {mi_pila.tope}")

4. Explicación del funcionamiento del código

- Clase Pila: define la estructura de datos mediante una lista llamada elementos, una variable tope y una capacidad máxima.

- Método init: inicializa la pila vacía, establece la capacidad máxima y asigna el valor inicial TOPE = 0. Los dos guiones bajos antes y después de init son necesarios para que Python reconozca correctamente el constructor.

- Método insertar: comprueba si la pila llegó a su capacidad máxima. Si hay espacio, agrega el elemento mediante append() e incrementa el TOPE en 1.

- Método eliminar: verifica si la pila está vacía. Si lo está, muestra el error de subdesbordamiento y devuelve None. Si contiene elementos, utiliza pop() para extraer el último elemento y disminuye el TOPE en 1.

- Ejecución de las operaciones: realiza los nueve incisos en el orden solicitado y guarda los elementos extraídos en las variables correspondientes.

- Resultado final: muestra los elementos que permanecen en la pila y el valor del TOPE.

5. Resultado final esperado

Al ejecutar el código, al final debe aparecer:

--- RESULTADO FINAL ---
Elementos finales en la pila: ['V', 'R']
Cantidad de elementos: 2
Valor final del TOPE: 2

Durante la ejecución también aparecerá el mensaje de subdesbordamiento en el inciso e, porque la pila está vacía en ese momento.

6. Conclusión

La pila termina con dos elementos, V y R, y el valor final del TOPE es 2. Durante la secuencia ocurre un subdesbordamiento al intentar eliminar un elemento de una pila vacía. No se presenta desbordamiento porque nunca se supera la capacidad máxima de 8 elementos.
