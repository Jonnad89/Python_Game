# Python 2D Arcade Game (Pygame)

## Project Overview

This project is a small, functional **2D arcade game** developed using the **Pygame** library in Python. It serves as a strong demonstration of object-oriented programming (OOP) principles and core software engineering concepts applied to real-time development.

## Key Features & Functionality

* **Game Loop Implementation:** Manages all rendering, state updates, and event processing within a clean, efficient game loop.
* **Event Handling:** Implementation of event listeners to process real-time user input (keyboard and/or mouse).
* **Object-Oriented Design:** Uses classes (e.g., Player, Enemy, GameState) to manage game elements, ensuring a modular and scalable codebase.
* **State Management:** Controls game flow, including tracking the score, managing lives, and handling transitions between states (e.g., Start Screen, Game Over).
* **Collision Detection:** Implementation of logical checks to determine interactions between game objects (e.g., player and boundaries, player and enemies).

## Tech Stack

* **Language:** Python 3.x
* **Libraries:** Pygame
* **Core Concepts:** Object-Oriented Programming (OOP), Event-Driven Architecture, Game Physics (Basic).

## Installation and Setup

### **Prerequisites**

You must have Python 3.x installed.

### **Steps**

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Jonnad89/Python_Game](https://github.com/Jonnad89/Python_Game)
    cd Python_Game
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Game:**
    ```bash
    python [Your Main Game File Name].py
    ```




## Spanish ##

Este proyecto consiste en la creación de un juego simple utilizando la biblioteca PyGame en Python. El objetivo es desarrollar un juego básico con funcionalidades mínimas que demuestren el uso de PyGame y sus capacidades.

## Funcionalidades del juego

- **Jugador controlable:** El jugador puede moverse horizontalmente utilizando las teclas izquierda y derecha.
- **Enemigos:** Hay enemigos que caen desde arriba y el jugador debe colisionar con ellos.
- **Colisión:** Cuando el jugador y un enemigo colisionan, se imprime un mensaje indicando la colisión y se incrementa el puntaje.
- **Pausa:** Al presionar la tecla "Enter", el juego entra en pausa y se muestra un mensaje en pantalla. Al volver a presionar "Enter", se reanuda el juego.

## Instrucciones para ejecutar el juego

1. Asegúrate de tener Python instalado en tu computadora.
2. Instala la biblioteca PyGame ejecutando `pip install pygame` en tu terminal.
3. Ejecuta el script `python_game.py` para iniciar el juego.

## Funciones personalizadas

El código incluye funciones para dibujar al jugador y al enemigo, manejar el movimiento del jugador, detectar colisiones, mostrar el puntaje y controlar la pausa.

## Mejoras futuras

Este proyecto es un punto de partida y puede mejorarse añadiendo más funcionalidades como puntajes más elaborados, niveles, gráficos y sonidos adicionales.
