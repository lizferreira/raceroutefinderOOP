from collections import deque

# Crear clases para el Mapa y la Calculadora de camino mas corto
class Mapa:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.mapa = [[0 for _ in range(columnas)] for _ in range(filas)]  # Inicializa un mapa vacío
    # Muestra el mapa marcando la ruta mas corta '*' si existe
    def mostrar(self, ruta=None):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.mapa[i][j] == 1:
                    print("x", end=" ")  # Obstáculo tipo 1: edificio
                elif self.mapa[i][j] == 2:
                    print("~", end=" ")  # Obstáculo tipo 2: agua
                elif self.mapa[i][j] == 3:
                    print("#", end=" ")  # Obstáculo tipo 3: área bloqueada
                elif ruta and (i, j) in ruta:
                    print("*", end=" ")  # Marca la ruta con '*'
                else:
                    print(".", end=" ")  # Espacio vacío
            print()
    # Permite al usuario agregar obstaculos al mapa
    def agregar_obstaculos(self):
        print("\nIngresar las coordenadas y tipo de obstáculos (0: carretera, 1: edificio, 2: agua, 3: área bloqueada, 'fin' para terminar):")
        while True:
            entrada = input("x,y,tipo de obstáculo: ")
            if entrada.lower() == 'fin':
                break
            coordenadas = entrada.split(',')
            if len(coordenadas) != 3:
                print('Formato incorrecto. Debes ingresar dos números separados por coma.')
                continue
            x, y, tipo_obstaculo = int(coordenadas[0]), int(coordenadas[1]), int(coordenadas[2])
            if 0 <= x < self.filas and 0 <= y < self.columnas:
                self.mapa[x][y] = tipo_obstaculo
            else:
                print('Coordenadas fuera de rango.')
    # Verifica si una posicion en el mapa es accesible
    def es_accesible(self, x, y):
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            return self.mapa[x][y] == 0 or self.mapa[x][y] == 2  # Carretera (0) o agua (2) son accesibles
        return False
    # Solicita al usuario puntos validos dentro del rango del mapa
    def obtener_puntos(self):
        while True:
            fila = int(input("x: "))
            columna = int(input("y: "))
            if 0 <= fila < self.filas and 0 <= columna < self.columnas:
                return fila, columna
            else:
                print("Coordenadas inválidas. Están fuera del rango.")

class CalculadoraRutas:
    def __init__(self, mapa):
        self.mapa = mapa
    # Calcula la ruta mas corta usando BFS
    def calcular_ruta(self, inicio, final):
        fila_busqueda = deque([(inicio, [inicio])])
        explorados = set([inicio])
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Direcciones arriba, abajo, izquierda, derecha
        
        while fila_busqueda:
            (actual, ruta) = fila_busqueda.popleft()
            if actual == final:
                return ruta
            for direccion in direcciones:
                vecino_fila = actual[0] + direccion[0]
                vecino_columna = actual[1] + direccion[1]
                if self.mapa.es_accesible(vecino_fila, vecino_columna) and (vecino_fila, vecino_columna) not in explorados:
                    explorados.add((vecino_fila, vecino_columna))
                    fila_busqueda.append(((vecino_fila, vecino_columna), ruta + [(vecino_fila, vecino_columna)]))
        return None

# Parte principal
# Inicializar el mapa de la pista
pista = Mapa(5, 5)

# Mostrar pista inicial
print("\nMapa de la pista:")
pista.mostrar()

# Agregar obstaculos a la pista
pista.agregar_obstaculos()

# Mostrar pista actualizada
print("\nPista actualizada:")
pista.mostrar()

# Obtener puntos de inicio y final de la ruta
print("\nIngrese las coordenadas de inicio del pit stop:")
inicio = pista.obtener_puntos()
print("\nIngrese las coordenadas del final:")
final = pista.obtener_puntos()

# Calcular la ruta mas corta
calculadora = CalculadoraRutas(pista)
ruta = calculadora.calcular_ruta(inicio, final)

# Mostrar la ruta obtenida en la pista
if ruta:
    print(f"\nRuta más corta encontrada desde {inicio} hasta {final}")
    pista.mostrar(ruta)
else:
    print("\nNo existe una ruta disponible.")
