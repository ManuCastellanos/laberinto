# Laberinto en Llamas (beta)
## Información del proyecto
- **Autor:** Manuel Iniesta Castellanos
- **Versión**: Python 3.11.8
- **Asistente IA**: [GitHub Copilot](https://copilot.github.com/)

## Patrones de diseño utilizados (16 patrones usados)

### Factory Method
El patrón Factory Method proporciona una interfaz para crear objetos, pero permite a las subclases decidir qué clase instanciar. Implementado en el archivo [`Juego.py`](./Game/Juego.py)

### Decorator
El patrón Decorator adjunta responsabilidades adicionales a un objeto de manera dinámica. Implementado en los archivos [`Decorator.py`](./EM/Hoj/Decorator/DecoratorC.py) y [`Bomba.py`](./EM/Hoj/Decorator/Bomba.py)

### Strategy
El patrón Strategy define una familia de algoritmos, encapsula cada uno y los hace intercambiables. Implementado en la carpeta [Mode](./Mode/).

### Composite
El patrón Composite compone objetos en estructuras de árbol para representar jerarquías de parte-todo. Implementado en el archivo [`Contenedor.py`](./EM/Container/Contenedor.py).

### Iterator
El patrón Iterator proporciona una forma de acceder a los elementos de un objeto agregado secuencialmente sin exponer su representación subyacente. Implementado en el archivo [`ElementoMapa.py`](./EM/ElementoMapa.py) y [`Orientación.py`](./Orientation/Orientacion.py).

### Template Method
El patrón Template Method define el esqueleto de un algoritmo en una operación, aplazando algunos pasos a las subclases sin variar la estructura del algoritmo. Implementado en el archivo [`Modo.py`](./Mode/Modo.py).

### Abstract Factory
El patrón Abstract Factory proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. Implementado en el archivo [`LaberintoAFactory.py`](./LaberintoAFactory.py).

### Singleton
El patrón Singleton asegura que una clase solo tenga una instancia y proporciona un punto de acceso global a ella. Implementado en los archivos [`Norte.py`](./Orientation/Norte.py), [`Sur.py`](./Orientation/Sur.py), [`Este.py`](./Orientation/Este.py) y [`Oeste.py`](./Orientation/Oeste.py).

### Builder
El patrón Builder separa la construcción de un objeto complejo de su representación para que el mismo proceso de construcción pueda crear diferentes representaciones. Implementado en los archivos [`Director.py`](./Builder/Director.py) y [`LaberintoBuilder.py`](./Builder/LaberintoBuilder.py). Se pueden ver los archivos para crear laberintos en la carpeta [JSON](./JSON/).

### Proxy
El patrón Proxy proporciona un sustituto o representante de otro objeto para controlar el acceso a él. Esto es útil cuando la creación de un objeto es costosa en términos de tiempo o recursos y quieres retrasar esta creación hasta que sea realmente necesario. Implementado en el archivo [`Tunel.py`](./EM/Hoj/Tunel.py).

### Adapter
El patrón Adapter convierte la interfaz de una clase en otra interfaz que los clientes esperan. Permite que las clases trabajen juntas que de otra manera no podrían debido a interfaces incompatibles. Implementado en el archivo [`Adapter.py`](Adapter\Adapter.py).

### State
El patrón de diseño State permite a un objeto alterar su comportamiento cuando su estado interno cambia. Define una serie de clases que representan los diferentes estados posibles de un objeto y proporcionauna interfaz común para cambiar entre estos estados. Implementado en: [`State.py`](State\Estado.py).

### Bridge
Patrón que desacopla una abstracción de su implementación de modo que las dos puedan variar de forma independiente. Implementado en [`Bridge`](Bridge\Forma.py) y [`Cuadrado`](Bridge\Cuadrado.py).
 
### Mediator
Patrón que define un objeto que encapsula la interacción entre un conjunto de objetos. Promueve un acoplamiento débil al evitar que los objetos tengan referencia al resto de objetos explícita. Implementado en [`Juego.py`](./Game/Juego.py), [`Ente.py`](./Entes/Ente.py).

### Prototype
Patrón que especifica el tipo de objetos a crear utilizando una instancia prototípica, y los crea copiando este prototipo.  Implementado en [`Juego.py`](./Game/Juego.py)

### Command
Patrón que encapsula una petición como un objeto, permitiendo parametrizar a los clientes con diferentes peticiones y soportar operaciones deshacer. Implementado en [Comandos](./Comandos).


## Diagrama de Diseño usando StarUML
<img src=https://github.com/ManuCastellanos/laberinto/blob/main/LaberintoFinished.png?raw=true>>