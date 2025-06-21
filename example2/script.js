/**
 * Snake Game - Main Game Logic
 * A classic snake game implementation using HTML5 Canvas
 */

class SnakeGame {
    constructor() {
        try {
            this.canvas = document.getElementById('gameCanvas');
            if (!this.canvas) {
                throw new Error('Canvas element not found');
            }
            
            this.ctx = this.canvas.getContext('2d');
            if (!this.ctx) {
                throw new Error('Could not get 2D context');
            }
            
            this.gridSize = 20;
            this.tileCount = this.canvas.width / this.gridSize;
            
            // Game state
            this.gameRunning = false;
            this.gamePaused = false;
            this.score = 0;
            this.highScore = localStorage.getItem('snakeHighScore') || 0;
            
            // Snake properties
            this.snake = [{x: 10, y: 10}];
            this.snakeLength = 1;
            this.velocityX = 0;
            this.velocityY = 0;
            
            // Food properties
            this.foodX = 15;
            this.foodY = 15;
            
            // Game speed
            this.gameSpeed = 150;
            this.lastRenderTime = 0;
            
            // Debug properties for boundary crossing
            this.boundaryCrossCount = 0;
            this.lastBoundaryCrossTime = 0;
            
            console.log('SnakeGame initialized successfully');
            
            // Initialize game
            this.initializeGame();
            this.setupEventListeners();
            this.updateHighScoreDisplay();
            
        } catch (error) {
            console.error('Error initializing SnakeGame:', error);
        }
    }
    
    /**
     * Initialize the game and set up initial state
     */
    initializeGame() {
        this.drawGame();
        this.showOverlay('Snake Game', 'Press Space to start');
    }
    
    /**
     * Set up event listeners for keyboard and button controls
     */
    setupEventListeners() {
        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            this.handleKeyPress(e);
        });
        
        // Button controls
        document.getElementById('startButton').addEventListener('click', () => {
            this.startGame();
        });
        
        document.getElementById('pauseButton').addEventListener('click', () => {
            this.togglePause();
        });
        
        document.getElementById('restartButton').addEventListener('click', () => {
            this.restartGame();
        });
    }
    
    /**
     * Handle keyboard input for game controls
     * @param {KeyboardEvent} e - Keyboard event
     */
    handleKeyPress(e) {
        if (!this.gameRunning && e.code === 'Space') {
            e.preventDefault();
            this.startGame();
            return;
        }
        
        if (this.gameRunning && e.code === 'Space') {
            e.preventDefault();
            this.togglePause();
            return;
        }
        
        if (this.gamePaused) return;
        
        // Movement controls
        switch(e.code) {
            case 'ArrowUp':
            case 'KeyW':
                if (this.velocityY !== 1) {
                    this.velocityX = 0;
                    this.velocityY = -1;
                }
                break;
            case 'ArrowDown':
            case 'KeyS':
                if (this.velocityY !== -1) {
                    this.velocityX = 0;
                    this.velocityY = 1;
                }
                break;
            case 'ArrowLeft':
            case 'KeyA':
                if (this.velocityX !== 1) {
                    this.velocityX = -1;
                    this.velocityY = 0;
                }
                break;
            case 'ArrowRight':
            case 'KeyD':
                if (this.velocityX !== -1) {
                    this.velocityX = 1;
                    this.velocityY = 0;
                }
                break;
        }
    }
    
    /**
     * Start the game
     */
    startGame() {
        try {
            console.log('Starting game...');
            this.gameRunning = true;
            this.gamePaused = false;
            
            // Start snake moving to the right if it's not already moving
            if (this.velocityX === 0 && this.velocityY === 0) {
                this.velocityX = 1;
                this.velocityY = 0;
                console.log('Snake started moving to the right');
            }
            
            this.hideOverlay();
            console.log('Game started successfully');
            this.gameLoop();
        } catch (error) {
            console.error('Error starting game:', error);
        }
    }
    
    /**
     * Toggle pause state
     */
    togglePause() {
        if (!this.gameRunning) return;
        
        this.gamePaused = !this.gamePaused;
        const pauseButton = document.getElementById('pauseButton');
        pauseButton.textContent = this.gamePaused ? 'Resume' : 'Pause';
        
        if (!this.gamePaused) {
            this.gameLoop();
        }
    }
    
    /**
     * Restart the game
     */
    restartGame() {
        this.resetGame();
        this.startGame();
    }
    
    /**
     * Reset game state to initial values
     */
    resetGame() {
        this.snake = [{x: 10, y: 10}];
        this.snakeLength = 1;
        this.velocityX = 0;
        this.velocityY = 0;
        this.score = 0;
        this.gameRunning = false;
        this.gamePaused = false;
        this.generateFood();
        this.updateScoreDisplay();
        
        const pauseButton = document.getElementById('pauseButton');
        pauseButton.textContent = 'Pause';
    }
    
    /**
     * Main game loop
     */
    gameLoop(currentTime = 0) {
        if (!this.gameRunning || this.gamePaused) return;
        
        window.requestAnimationFrame((time) => this.gameLoop(time));
        
        const secondsSinceLastRender = (currentTime - this.lastRenderTime) / 1000;
        if (secondsSinceLastRender < this.gameSpeed / 1000) return;
        
        this.lastRenderTime = currentTime;
        
        try {
            this.update();
            this.drawGame();
        } catch (error) {
            console.error('Error in game loop:', error);
            this.gameRunning = false;
        }
    }
    
    /**
     * Update game state
     */
    update() {
        try {
            // Move snake
            const newHead = {
                x: this.snake[0].x + this.velocityX,
                y: this.snake[0].y + this.velocityY
            };
            
            // Handle boundary wrapping - snake appears on opposite side
            if (newHead.x < 0 || newHead.x >= this.tileCount || newHead.y < 0 || newHead.y >= this.tileCount) {
                // Track boundary crossing without showing overlay
                this.boundaryCrossCount++;
                this.lastBoundaryCrossTime = Date.now();
                
                // Wrap position to opposite side immediately
                if (newHead.x < 0) {
                    newHead.x = this.tileCount - 1;
                } else if (newHead.x >= this.tileCount) {
                    newHead.x = 0;
                }
                if (newHead.y < 0) {
                    newHead.y = this.tileCount - 1;
                } else if (newHead.y >= this.tileCount) {
                    newHead.y = 0;
                }
                
                console.log(`Boundary crossing #${this.boundaryCrossCount} completed`);
            }
            
            // Check for self collision
            for (let i = 0; i < this.snake.length; i++) {
                if (this.snake[i].x === newHead.x && this.snake[i].y === newHead.y) {
                    this.gameOver();
                    return;
                }
            }
            
            // Add new head
            this.snake.unshift(newHead);
            
            // Check for food collision
            if (newHead.x === this.foodX && newHead.y === this.foodY) {
                this.score += 10;
                this.snakeLength++;
                this.generateFood();
                this.updateScoreDisplay();
                
                // Increase game speed
                if (this.score % 50 === 0) {
                    this.gameSpeed = Math.max(50, this.gameSpeed - 10);
                }
            } else {
                // Remove tail if no food eaten
                this.snake.pop();
            }
        } catch (error) {
            console.error('Error in update method:', error);
            throw error;
        }
    }
    
    /**
     * Draw the game on canvas
     */
    drawGame() {
        // Clear canvas
        this.ctx.fillStyle = '#f7fafc';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw snake
        this.ctx.fillStyle = '#3182ce';
        this.snake.forEach((segment, index) => {
            if (index === 0) {
                // Draw head with different color
                this.ctx.fillStyle = '#2c5282';
            } else {
                this.ctx.fillStyle = '#3182ce';
            }
            this.ctx.fillRect(segment.x * this.gridSize, segment.y * this.gridSize, 
                            this.gridSize - 2, this.gridSize - 2);
        });
        
        // Draw food
        this.ctx.fillStyle = '#e53e3e';
        this.ctx.fillRect(this.foodX * this.gridSize, this.foodY * this.gridSize, 
                         this.gridSize - 2, this.gridSize - 2);
        
        // Draw grid (optional)
        this.drawGrid();
        
        // Draw debug information
        this.drawDebugInfo();
    }
    
    /**
     * Draw grid lines for better visibility
     */
    drawGrid() {
        this.ctx.strokeStyle = '#e2e8f0';
        this.ctx.lineWidth = 1;
        
        for (let i = 0; i <= this.tileCount; i++) {
            // Vertical lines
            this.ctx.beginPath();
            this.ctx.moveTo(i * this.gridSize, 0);
            this.ctx.lineTo(i * this.gridSize, this.canvas.height);
            this.ctx.stroke();
            
            // Horizontal lines
            this.ctx.beginPath();
            this.ctx.moveTo(0, i * this.gridSize);
            this.ctx.lineTo(this.canvas.width, i * this.gridSize);
            this.ctx.stroke();
        }
    }
    
    /**
     * Draw debug information on canvas
     */
    drawDebugInfo() {
        this.ctx.fillStyle = '#000000';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'left';
        
        const debugY = 20;
        this.ctx.fillText(`Boundary Crosses: ${this.boundaryCrossCount}`, 10, debugY);
        
        if (this.lastBoundaryCrossTime > 0) {
            const timeSinceLastCross = Math.floor((Date.now() - this.lastBoundaryCrossTime) / 1000);
            this.ctx.fillText(`Time since last cross: ${timeSinceLastCross}s`, 10, debugY + 15);
        }
        
        // Show current snake position for debugging (with safety check)
        if (this.snake && this.snake.length > 0) {
            this.ctx.fillText(`Snake Head: (${this.snake[0].x}, ${this.snake[0].y})`, 10, debugY + 30);
        } else {
            this.ctx.fillText(`Snake Head: No snake`, 10, debugY + 30);
        }
    }
    
    /**
     * Generate new food position
     */
    generateFood() {
        let newFoodX, newFoodY;
        let validPosition = false;
        
        while (!validPosition) {
            newFoodX = Math.floor(Math.random() * this.tileCount);
            newFoodY = Math.floor(Math.random() * this.tileCount);
            
            validPosition = true;
            
            // Check if food position overlaps with snake
            for (let segment of this.snake) {
                if (segment.x === newFoodX && segment.y === newFoodY) {
                    validPosition = false;
                    break;
                }
            }
        }
        
        this.foodX = newFoodX;
        this.foodY = newFoodY;
    }
    
    /**
     * Handle game over
     */
    gameOver() {
        this.gameRunning = false;
        
        // Update high score
        if (this.score > this.highScore) {
            this.highScore = this.score;
            localStorage.setItem('snakeHighScore', this.highScore);
            this.updateHighScoreDisplay();
        }
        
        this.showOverlay('Game Over!', `Score: ${this.score}`);
    }
    
    /**
     * Show overlay with custom title and message
     * @param {string} title - Overlay title
     * @param {string} message - Overlay message
     */
    showOverlay(title, message) {
        const overlay = document.getElementById('gameOverlay');
        const titleElement = document.getElementById('overlayTitle');
        const messageElement = document.getElementById('overlayMessage');
        
        titleElement.textContent = title;
        messageElement.textContent = message;
        overlay.classList.remove('hidden');
    }
    
    /**
     * Hide the overlay
     */
    hideOverlay() {
        const overlay = document.getElementById('gameOverlay');
        overlay.classList.add('hidden');
    }
    
    /**
     * Update score display
     */
    updateScoreDisplay() {
        document.getElementById('score').textContent = this.score;
    }
    
    /**
     * Update high score display
     */
    updateHighScoreDisplay() {
        document.getElementById('highScore').textContent = this.highScore;
    }
}

// Initialize game when page loads
document.addEventListener('DOMContentLoaded', () => {
    new SnakeGame();
}); 