# 🏓 Breakout / Arkanoid - Pygame

Breakout desarrollado en Python utilizando Pygame como proyecto práctico para reforzar fundamentos de programación, game loops, detección de colisiones y simulación de física 2D.

El proyecto implementa rebotes dinámicos de la pelota, múltiples niveles, sistema de vidas, puntuación y un récord persistente almacenado localmente.

## 🎮 Características

- Game Loop a 60 FPS.
- Control de la paleta con límites de pantalla.
- Movimiento de la pelota mediante vectores `VX` y `VY`.
- Rebote en paredes.
- Rebote dinámico en la paleta dependiendo de la posición del impacto.
- Detección de colisiones con bloques utilizando la posición anterior de la pelota.
- Generación dinámica de bloques por filas y columnas.
- 5 niveles con diferentes configuraciones.
- Transiciones entre niveles.
- Sistema de vidas.
- Game Over y Game Win.
- Sistema de puntuación.
- High Score persistente.
- Reinicio de partida mediante `ENTER`.

## 🕹️ Controles

| Tecla | Acción |
|---|---|
| `←` | Mover paleta a la izquierda |
| `→` | Mover paleta a la derecha |
| `↑` | Lanzar la pelota |
| `ENTER` | Reiniciar después de Game Over / Game Win |
| `ESC` | Salir del juego |

## 🛠️ Tecnologías

- Python
- Pygame
- Git / GitHub

## 📦 Instalación

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/Alex040901/Breakout.git
cd breakout
```

### Crear un entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Instalar las dependencias

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

Con el entorno virtual activado:

```bash
python main.py
```

## 📁 Estructura del proyecto

```text
breakout/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── breakout_highscore.txt
```

`breakout_highscore.txt` se genera localmente para almacenar el récord y está excluido del repositorio mediante `.gitignore`.