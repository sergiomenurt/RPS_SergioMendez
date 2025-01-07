# RPS_SergioMendez

# Juego Piedra, Papel o Tijera

Este proyecto está basado en el juego "Piedra, Papel o Tijera". Este permite que un usuario compita contra la computadora en múltiples rondas. Al alcanzar las 6 rondas, la computadora intenta predecir las elecciones del usuario basándose en su historial de elecciones anteriores. El objetivo del proyecto es ofrecer el ocio de poder disputar un juego de la mejor manera posible contra un ordenador que actúa de manera inteligente

# 1. Especificación do contorna de tarefas



| **Contorno de tareas** | **Completamente/Parcialmente Observable** | **Agentes**    | **Determinista/Estocástico** | **Episódico/Secuencial** | **Estático/Dinámico** | **Discreto/Continuo** | **Conocido/Desconocido** |
|:----------------------:|:---------------------------------------:|:--------------:|:---------------------------:|:------------------------:|:---------------------:|:----------------------:|:-------------------------:|
| **RPS**                | Parcialmente                            | Multiagente     | Estocástico                 | Episódico                | Estático              | Discreto               | Conocido                  |

**Completamente/Parcialmente Observable:** Parcialmente, ya que el jugador ve su propia acción y la del ordenador, pero no sabe cómo la computadora predice que hará.

**Agentes:** 
Multiagente, en este caso serán el jugador y el ordenador, los cuáles jugarán el uno contra el otro.

**Determinista/Estocástico:** 
Estocástico, ya que el ordenador elegirá de manera aleatoria o basándose en el historial de rondas anteriores(en casos utilizando un randomizador de elección en estos casos).

**Episódico/Secuencial:** 
Episódico, cada ronda de juego será diferente y no afectará al resto.

**Estático/Dinámico:** 
Estático, ya que las reglas del juego no cambiarán de una ronda a otra.

**Discreto/Continuo:** 
Discreto, ya que sólo existen tres elecciones posibles en el juego.

**Conocido/Desconocido:** 
Conocido, ambos jugadores conoceran las reglas y el entorno del juego.

# 2. Identificación do tipo de axente e estrutura

El tipo de agente va a ser basado en modelos y realizará una cción en cuanto a información pasada guardada

# 3. Implementación en Python

Será simple, solo hará falta un entorno (en mi caso utilizo conda), y solo habrá una clase. Lo más complejo pueden ser los tests.


# 4. Extensión ao RPS + Lizard Spock

No cambiará mucho código, será una implementación más al códifo de RPS.py y en los tests par que funcionen las nuevas opciones del juego.(Importante: Explicar juego(ver en que parte del README se explica))