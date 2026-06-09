# Pygame Flappy Bird

A Python implementation of the popular Flappy Bird game using Pygame, featuring custom sprite animations, collision detection, and score tracking.

## 🎮 Game Overview

This is a recreation of the classic Flappy Bird game where you navigate a player character through obstacles by pressing the spacebar to jump. Avoid collision with the pipes and try to achieve the highest score!

### Features
- **Sprite Animation**: Animated player character with multiple frames
- **Collision Detection**: Advanced hitbox collision system for accurate gameplay
- **Score Tracking**: Keep track of your score as you pass through obstacles
- **Obstacle Generation**: Randomized obstacle placement for varied gameplay
- **Physics**: Realistic gravity and jump mechanics

## 📋 Requirements

- Python 3.6+
- Pygame 2.0+

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ignacyN1234/pygame-flappy-bird.git
cd pygame-flappy-bird
```

### 2. Install Dependencies
Using pip:
```bash
pip install -r requirements.txt
```

Or install pygame directly:
```bash
pip install pygame
```

### 3. Run the Game
```bash
python main.py
```

## 🎮 How to Play

- **Start**: Run the game with `python main.py`
- **Jump**: Press and hold the **SPACEBAR** to make the player jump
- **Objective**: Navigate through the obstacles without hitting them
- **Scoring**: Earn 1 point for each obstacle pair you successfully pass
- **Game Over**: The game ends if you hit an obstacle or go out of bounds
- **Final Score**: Your final score is printed to the console when the game ends

## 📁 Project Structure

```
pygame-flappy-bird/
├── main.py              # Main game file
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── assets/             # Game sprites and images
│   ├── Sprite-0001.png
│   ├── sprite3.png
│   ├── sprite5.png
│   ├── sprite1.png
│   └── sprite76.png
└── .gitignore
```

## 🎨 Game Components

### Gracz (Player)
The controllable character that navigates through obstacles.
- **Velocity**: Affected by gravity and jump mechanics
- **Animation**: Cycles through sprite frames for visual feedback
- **Collision**: Detects collisions with obstacles and screen boundaries

### Obstacles
Two types of obstacles that move toward the player:
1. **Obstacle1** (obstacle_sprite1): Lower pipe
2. **Obstacle2** (obstacle_sprite2): Upper pipe

Both obstacles have randomized vertical positioning and move horizontally across the screen.

## 🎯 Controls

| Key | Action |
|-----|--------|
| **SPACEBAR** | Jump/Flap |
| **X** (close window) | Quit Game |

## ⚙️ Game Settings

You can customize the game experience by modifying values in `main.py`:

- **WIDTH / HEIGHT**: Screen dimensions (currently 1000x1000)
- **SCALE**: Player sprite scale factor (currently 4)
- **scale_for_obstacle**: Obstacle sprite scale (currently 30)
- **acceleration**: Gravity acceleration (currently 0.2)
- **velocityy**: Jump velocity (currently -6)

## 🐛 Troubleshooting

### Assets not found error
Ensure that all sprite files exist in the `assets/` directory:
- Sprite-0001.png
- sprite3.png
- sprite5.png
- sprite1.png
- sprite76.png

### Game runs slowly
Try reducing the screen size or adjusting the frame rate by modifying `clock.tick(60)` in main.py (lower value = lower frame rate).

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests with improvements!

---

**Enjoy the game! 🎉**
