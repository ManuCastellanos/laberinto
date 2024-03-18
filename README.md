# Laberinto en Llamas (beta)
## Información del proyecto
- **Autor:** Manuel Iniesta Castellanos
- **Versión**: Python 3.11.8
- **Asistente IA**: [GitHub Copilot](https://copilot.github.com/)

## Patrones de diseño utilizados (9 patrones usados)

### Factory Method
El patrón Factory Method proporciona una interfaz para crear objetos, pero permite a las subclases decidir qué clase instanciar. Implementado en el archivo [`Juego.py`](./Game/Juego.py)

### Decorator
El patrón Decorator adjunta responsabilidades adicionales a un objeto de manera dinámica. Implementado en el archivo [`Decorator.py`](./EM/Hoj/Deco/Decorator.py) y [`Bomba.py`](./EM/Hoj/Deco/Bomba.py)

### Strategy
El patrón Strategy define una familia de algoritmos, encapsula cada uno y los hace intercambiables. Implementado en el archivo [`Bicho.py`](./Bicho.py).

### Composite
El patrón Composite compone objetos en estructuras de árbol para representar jerarquías de parte-todo. Implementado en el archivo [`Contenedor.py`](./EM/Cont/Contenedor.py).

### Iterator
El patrón Iterator proporciona una forma de acceder a los elementos de un objeto agregado secuencialmente sin exponer su representación subyacente. Implementado en el archivo [`ElementoMapa.py`](./EM/ElementoMapa.py) y [`Orientación.py`](./Orientation/Orientacion.py).

### Template Method
El patrón Template Method define el esqueleto de un algoritmo en una operación, aplazando algunos pasos a las subclases. Implementado en el archivo [`Modo.py`](./Mode/Modo.py).

### Abstract Factory
El patrón Abstract Factory proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. Implementado en el archivo [`LaberintoAFactory.py`](./LaberintoAFactory.py).

### Singleton
El patrón Singleton asegura que una clase solo tenga una instancia y proporciona un punto de acceso global a ella. Implementado en los archivos [`Norte.py`](./Orientation/Norte.py), [`Sur.py`](./Orientation/Sur.py), [`Oeste.py`](./Orientation/Este.py) y [`Este.py`](./Orientation/Oeste.py).

### Builder
El patrón Builder separa la construcción de un objeto complejo de su representación para que el mismo proceso de construcción pueda crear diferentes representaciones. Implementado en los archivos [`Director.py`](./Builder/Director.py) y [`LaberintoBuilder.py`](./Builder/LaberintoBuilder.py). Se pueden ver los archivos para crear laberintos en la carpeta [JSON](./JSON/).
