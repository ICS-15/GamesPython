# 🎮 Python Games

This repository contains two classic arcade games developed with **Python** and **Pygame** as part of a personal learning project.

The aim was to gain hands-on experience of game development concepts such as event handling, animation, collision detection and project organisation, all while creating fully playable games.
## Included Games

### 🐍 Snake

Control the snake, collect food, and survive as long as possible while trying to beat your highest score.

### 🧱 Brick Breaker

Move the paddle to keep the ball in play, destroy every brick, and earn the highest score you can.

## Project Structure

```text
GamesPython/
│
├── main.py                  # Game launcher
├── snake/                   # Snake game
├── brickBreaker/            # Brick Breaker game
├── utils/                   # Shared files
└── README.md
```

## Getting Started

### Requirements

* Python 3.11+
* Pygame
* cx_Freeze (optional, for creating an executable)

Install the required packages:

```bash
pip install pygame cx_Freeze
```

### Running the Project

Clone the repository:

```bash
git clone https://github.com/ICS-15/GamesPython.git
```

Open the project folder:

```bash
cd GamesPython
```

Start the launcher:

```bash
python main.py
```

From the launcher you can choose:

* **1** – Snake
* **2** – Brick Breaker
* **Esc** – Exit

## Learning Objectives

During this project I practiced:

* Developing games with Pygame
* Managing keyboard input
* Implementing collision detection
* Creating score systems
* Structuring a project with reusable modules
* Building a simple game launcher

## Building the Executable

To create an executable version of the project:

```bash
python setup.py build
```

## Author

**Inês Saragoça**

Created as a learning project to explore game development with Python and Pygame.
