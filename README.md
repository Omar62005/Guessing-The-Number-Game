# 🎯 Number Guessing Game

A simple and interactive Python-based number guessing game where players try to guess a randomly generated number between 1 and 50.

## 📋 Table of Contents
- [Features](#features)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Code Structure](#code-structure)
- [Example Gameplay](#example-gameplay)
- [Skills Demonstrated](#skills-demonstrated)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Random Number Generation**: Generates a random number between 1-50 for each game
- **Hint System**: Provides "higher" or "lower" feedback after each guess
- **Attempt Tracking**: Counts and displays the total number of attempts
- **User-Friendly Interface**: Clear instructions and welcoming messages
- **Personalized Experience**: Asks for player's name for a custom greeting

## 🎮 How to Play

1. Run the program
2. Enter your name when prompted
3. Guess a number between 1 and 50
4. Receive hints if your guess is incorrect:
   - "The right number is bigger than your guess" - Guess higher
   - "The right number is smaller than your guess" - Guess lower
5. Continue guessing until you find the correct number
6. Celebrate your victory and see your total attempts!

## 🚀 Installation

### Prerequisites
- Python 3.x installed on your system

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
   cd number-guessing-game
   ```

2. **No additional dependencies required** - uses only Python standard library


## 📖 Game Rules

- **Number Range:** 1 to 50 (inclusive)
- **Unlimited Attempts:** Keep guessing until you get it right
- **Hints Provided:** After each incorrect guess, you'll get a hint
- **Win Condition:** Guess the exact number to win

## 🏗️ Code Structure

```
number_guessing_game.py
├── generating_random()     # Generates random number (1-50)
├── game()                  # Main game logic and loop  
└── main()                  # Entry point, handles user greeting
```

### Functions Overview:

- **`generating_random()`:** Returns a random integer between 1 and 50
- **`game()`:** Handles the core game mechanics, user input, and feedback  
- **`main()`:** Manages user welcome, instructions, and starts the game

## 🎯 Example Gameplay

```
===== Guess The Number Game ======
==================================
Please Enter Your name : ALICE
Welcome ALICE !!!
Game Instructions : 
 => Try to guess the right number 
======================================================================================
Please Guess number between 1 and 50 : 25
The right number is bigger than your guess 
Please Guess number between 1 and 50 : 35
The right number is smaller than your guess 
Please Guess number between 1 and 50 : 30
YOU DID IT !!!!
You found the number correctly after 3 attempts
```

## 🛠️ Skills Demonstrated

This project showcases the following Python programming concepts:

### Basic Python Programming
- Variables and data types
- Input/output operations  
- String manipulation and formatting

### Control Flow
- Conditional statements (if/elif/else)
- While loops for game continuation
- Loop control and exit conditions

### Functions
- Function definition and calling
- Return statements
- Code organization and modularity

### Libraries
- Random number generation using `random` module

## 🚀 Future Enhancements

Potential improvements for the game:

- [ ] **Input Validation**: Handle non-numeric inputs gracefully
- [ ] **Difficulty Levels**: Different number ranges (Easy: 1-20, Hard: 1-100)
- [ ] **Play Again Feature**: Option to restart without closing the program
- [ ] **Score System**: Track best scores (fewest attempts)
- [ ] **High Score Persistence**: Save scores to a file
- [ ] **GUI Version**: Create a graphical interface using tkinter
- [ ] **Multiplayer Mode**: Two players taking turns



---

**Happy Guessing! 🎉**

*Created as a learning project to practice Python fundamentals and game development basics.*
