# Snakes and Ladders Game (Python - Tkinter)🎲🐍  

This project of **Snakes and Ladders** game implemented in **Python** using the **Tkinter** library for GUI development. It was developed as part of an integrated subject project during my **4th semester of CSE Undergrad**. The game provides a simple yet engaging experience by simulating the classic board game with a graphical interface, automated dice rolls, and turn-based player movement.

## Implementation Details  

The game follows the standard Snakes and Ladders rules, where players roll a dice and move accordingly, encountering ladders that take them up and snakes that bring them down. The game board is drawn using Tkinter’s **Canvas** widget, and player positions update dynamically based on dice rolls.

### **Key Features and Functionality**  

- **Graphical Board Creation**:  
  The board consists of 100 tiles arranged in a **10x10 grid**, with alternating colors for better visibility. Each tile is numbered, and the board follows the traditional snake-and-ladder layout.  
- **Snakes and Ladders Implementation**:  
  A **dictionary** stores predefined positions of snakes and ladders. When a player lands on a snake's mouth or the bottom of a ladder, their position updates accordingly.  
- **Player Movement**:  
  Each player starts at position 0 and can enter the board only by rolling a six. Players take turns rolling a dice (using Python’s `random.randint(1, 6)`) and move forward based on the result. The game ensures players do not exceed tile 100, enforcing the exact number needed to win.  
- **Turn-Based Gameplay**:  
  The game supports up to **four players**, and turns cycle automatically. The interface displays messages indicating each player's roll and movement updates.  
- **Game Win Condition**:  
  When a player reaches tile 100, a message is displayed announcing the winner, and the game stops further dice rolls.  

### **Technology Stack**  

- **Python**: Core language used for game logic and implementation.  
- **Tkinter**: Used for creating the graphical user interface, handling the board, and displaying real-time updates.  
- **Random Module**: Used for simulating dice rolls to add randomness to the gameplay.  
