# Race Route Finder (Refactorizado con OOP)
Esta implementacion en Python simula una pista de carreras con obstáculos y un buscador de rutas de paradas en boxes. El objetivo es encontrar la ruta más corta desde un punto de partida hasta un punto de llegada, evitando obstáculos y áreas bloqueadas utilizando el algoritmo Breadth-First Search (BFS). La pista está representada por un mapa bidimensional, donde cada celda representa una ubicación específica en la pista. 

## Características:
- Simula una pista de carreras con varios obstáculos (edificios, agua y áreas bloqueadas) en un mapa bidimensional (2D).
- Permite a los usuarios agregar obstáculos a la pista modificando el mapa.
- Encuentra la ruta más corta desde un punto inicial hasta un punto final utilizando el algoritmo BFS.
- Muestra el mapa y la ruta calculada.

## Estructura:
El proyecto ha sido refactorizado para seguir los principios de la Programación Orientada a Objetos (OOP), utilizando dos clases principales: Mapa y CalculadoraRutas.

### Clase `Mapa`:
La clase Mapa representa el entorno de la pista de carreras y proporciona métodos para gestionar y visualizar el mapa:

1. Inicialización del Mapa: Se inicializa con un número de filas y columnas, creando un mapa vacío o con obstáculos predefinidos.

2. Mostrar el Mapa: Permite visualizar el mapa en la consola, mostrando los obstáculos y la ruta más corta si se ha calculado.

3. Agregar Obstáculos: Permite al usuario agregar obstáculos al mapa, especificando las coordenadas y el tipo de obstáculo (carretera, edificio, agua, área bloqueada).

4. Verificar Accesibilidad: Determina si una posición específica en el mapa es accesible (carretera o agua).

5. Obtener Puntos: Solicita al usuario coordenadas válidas dentro del rango del mapa.

### Clase `CalculadoraRutas`:
La clase `CalculadoraRutas` se encarga de calcular la ruta más corta utilizando el algoritmo BFS:
1. Inicialización: Recibe un objeto `Mapa` para calcular las rutas en ese contexto específico.
2. Calcular Ruta: Implementa el algoritmo BFS para encontrar la ruta más corta desde un punto de inicio hasta un punto final en el mapa, evitando obstáculos.

## Funcionalidades principales:
1. Inicialización de la pista: La pista se inicializa con un mapa predefinido que puede ser modificado por el usuario agregando diferentes tipos de obstáculos. La pista se representa como una matriz bidimensional donde:
- 0 representa una carretera transitable.
- 1 representa un edificio u obstáculo no transitable.
- 2 representa agua, que es transitable.
- 3 representa áreas bloqueadas temporalmente que no son transitables.

2. Mostrar la pista: La función `mostrar` permite visualizar el estado actual de la pista en la consola, mostrando los obstáculos y, si se ha calculado una ruta, marcándola con *.

3. Agregar obstaculos: Se pueden agregar obstáculos a la pista utilizando la función agregar_obstaculos. El usuario puede ingresar las coordenadas y el tipo de obstáculo (0, 1, 2 o 3).

4. Obtener puntos de inicio y final: El usuario debe ingresar las coordenadas del punto de inicio y del punto final para calcular la ruta utilizando la función `obtener_puntos`.

5. Calcular la ruta más corta: La función `calcular_ruta` utiliza el algoritmo BFS para encontrar la ruta más corta desde el punto de inicio hasta el punto final en la pista, evitando obstáculos. Si se encuentra una ruta, se muestra en la pista.

### Requisitos
- Python 3.x  
