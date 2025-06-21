# Snake Game

A classic Snake game implementation using HTML5 Canvas, JavaScript, and CSS. This web-based game features smooth animations, responsive design, and modern UI with boundary wrapping mechanics.

## Features

- 🐍 Classic snake gameplay mechanics
- 🌐 Boundary wrapping - snake appears on opposite side when hitting edges
- 🎮 Multiple control options (Arrow keys or WASD)
- ⏸️ Pause/Resume functionality
- 🏆 High score tracking with local storage
- 📱 Responsive design for mobile devices
- 🎨 Modern gradient UI design
- ⚡ Dynamic game speed increase
- 🎯 Visual grid for better gameplay

## How to Play

1. **Start the game**: Press Space or click "Start Game"
2. **Control the snake**: Use arrow keys or WASD to move
3. **Eat food**: Collect red food to grow and earn points
4. **Cross boundaries**: Snake can move through walls and appear on the opposite side
5. **Avoid self collision**: Don't hit your own body
6. **Pause**: Press Space or click "Pause" to pause/resume
7. **Restart**: Click "Restart" to start a new game

## Game Controls

### Keyboard Controls
- **Arrow Keys** or **WASD**: Move snake
- **Space**: Start game / Pause/Resume
- **R**: Restart game (alternative)

### Button Controls
- **Start Game**: Begin a new game
- **Pause/Resume**: Toggle game pause
- **Restart**: Reset and start new game

## Game Mechanics

- **Scoring**: 10 points per food eaten
- **Speed Increase**: Game speeds up every 50 points
- **Snake Growth**: Snake grows longer with each food eaten
- **Boundary Wrapping**: Snake can move through walls and appear on opposite side
- **Collision Detection**: Game ends only on self collision
- **High Score**: Best score saved in browser localStorage

## Technical Details

### Technologies Used
- **HTML5**: Canvas element for game rendering
- **CSS3**: Modern styling with gradients and animations
- **JavaScript ES6+**: Class-based game logic
- **Local Storage**: Persistent high score tracking

### Game Architecture
- **SnakeGame Class**: Main game controller
- **Canvas Rendering**: Smooth 60fps gameplay
- **Event-Driven**: Keyboard and button event handling
- **State Management**: Game state tracking and updates
- **Boundary Logic**: Wrapping mechanics for seamless gameplay

## File Structure

```
example2/
├── index.html      # Main HTML file
├── style.css       # CSS styling
├── script.js       # Game logic
└── README.md       # This file
```

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Installation

No installation required! Simply open `index.html` in a web browser to play.

```bash
# Optionally, serve with a local server for development
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

## Customization

### Changing Game Speed
Modify the `gameSpeed` property in the `SnakeGame` constructor:
```javascript
this.gameSpeed = 150; // Lower = faster
```

### Changing Grid Size
Modify the `gridSize` property:
```javascript
this.gridSize = 20; // Pixels per grid cell
```

### Changing Colors
Update the color values in `drawGame()` method:
```javascript
// Snake head color
this.ctx.fillStyle = '#2c5282';
// Snake body color  
this.ctx.fillStyle = '#3182ce';
// Food color
this.ctx.fillStyle = '#e53e3e';
```

### Boundary Behavior
The game currently uses boundary wrapping. To change to wall collision:
```javascript
// In the update() method, replace boundary wrapping with:
if (newHead.x < 0 || newHead.x >= this.tileCount || 
    newHead.y < 0 || newHead.y >= this.tileCount) {
    this.gameOver();
    return;
}
```

## Future Enhancements

- [ ] Sound effects
- [ ] Different difficulty levels
- [ ] Power-ups and special food
- [ ] Multiplayer support
- [ ] Leaderboard system
- [ ] Mobile touch controls
- [ ] Different snake skins
- [ ] Obstacle walls
- [ ] Toggle between boundary wrapping and wall collision

## License

This project is open source and available under the MIT License. 