# FINAL-TEAM-PROJECT-GAGFEST

# GAGFEST

Welcome to the **GAGFEST**, a collection of 12 mini-Pygames and AI applications developed using Python. This project offers a variety of interactive experiences, from fun and engaging games to AI-powered tools, all accessible through a user-friendly web interface.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Games and Applications](#games-and-applications)
  - [1. Colorful Python](#1-colorful-python)
  - [2. Guess Who I Am](#2-guess-who-i-am)
  - [3. Rainfall](#3-rainfall)
  - [4. Let's Draw Together](#4-lets-draw-together)
  - [5. Magic Bubble](#5-magic-bubble)
  - [6. Puzzle Game](#6-puzzle-game)
  - [7. Bury Me with Money](#7-bury-me-with-money)
  - [8. Make a Cloth Tiger](#8-make-a-cloth-tiger)
  - [9. Russian Roulette](#9-russian-roulette)
  - [10. AI Media Reviewer](#10-ai-media-reviewer)
  - [11. Praise and Roast AI](#11-praise-and-roast-ai)
  - [12. Deal With It](#12-deal-with-it)
- [Contributing](#contributing)
- [License](#license)


## Features

-   **Interactive Web Hub**: A Flask-based web interface to access all games and applications.
-   **Variety of Games**: Includes 10 mini-games developed with Pygame and Tkinter.
-   **AI Applications**: Integrates OpenAI's GPT models for generating ratings and reviews and interactive AI experiences.
-   **User-Friendly Interface**: Easy navigation with a visually appealing design.

## Demo

![GAGFEST SCREENSHOT](assets/images/GAGFEST_Screenshot.png)

## Installation

### Prerequisites

-   **Python 3.7** or higher
-   **pip** (Python package installer)
-   **Virtual Environment** (recommended)
-   **OpenAI API Key** (for AI functionalities)

### Setup Instructions

1.  **Clone the Repository**
2.  **Set Up a Virtual Environment**
3.  **Install Dependencies**

    Install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt 
    ```
5.  **Configure OpenAI API**
    
    For the AI applications to work, you need to set up your OpenAI API key:
    
    -   Sign up on [OpenAI](https://openai.com/index/openai-api/) to get an API key.
    -   In `app.py` and `11Praise and Roast AI.py`, replace `"dummy_key"` with your actual API key.
    -   Ensure the `openai.api_base` is set correctly (usually `"https://api.openai.com/v1"`).
6.  **Set Up Asset Files**
    
    -   Ensure all image and sound assets are placed in the correct directories as referenced in the code.
    -   Assets include images (`.png`, `.jpg`), sounds (`.wav`, `.mp3`), and other media files.

## Usage

1.  **Run the Flask Application**
    
    ```bash
    python app.py
    ```
    
    This will start the web server.
    
2.  **Access the Interactive Hub**
    
    Open your web browser and navigate to `http://localhost:5000/` to access the hub.
    
3.  **Play Games and Use Applications**
    
    -   Click on any game or application in the hub to launch it.
    -   Some games will open in a new window.
    -   For AI applications, follow the on-screen instructions.
4.  **Run the Praise and Roast AI Separately**
    
    The "Praise and Roast AI" application runs using Streamlit:
    
    -   Open a new terminal window.
        
    -   Navigate to the project directory.
        
    -   Run the Streamlit app:
        
        ```bash
        streamlit run "11Praise and Roast AI.py"
        ```
        
    -   Access it via `http://localhost:8501`.
        
## Games and Applications

### 1. Colorful Python

-   **Description**: An interactive cyberpunk-themed particle effect simulation. Experience a dynamic and colorful display where particles react to your mouse movements, creating mesmerizing patterns and visuals on the screen.
    
-   **Features**:
    -   **Particle Interaction**: Particles respond to mouse position and movement.
    -   **Dynamic Visuals**: Real-time rendering of particles with varying colors and velocities.
    -   **High-Resolution Graphics**: Adapts to different screen sizes for optimal display.
    -   **Background Gradient**: A visually appealing gradient that enhances the cyberpunk aesthetic.
-   **Technologies**: Pygame, NumPy, OpenCV.
    
-   **How to Play**:
    
    -   Simply move your mouse around the screen to influence the particle effects.
    -   Watch as particles move, collide, and create patterns in response to your movements.
    -   There are no objectives—just relax and enjoy the visuals.
-   **Instructions**:
    
    -   Run `1Colorful Python.py`.
    -   Ensure all required libraries are installed.
    -   Close the window or press `Esc` to exit.

### 2. Guess Who I Am

-   **Description**: A playful game where you click to reveal hints and guess the hidden character or profession. Each stage presents a new image concealed behind tiles. As you click, parts of the image are revealed through fun animations and sound effects.
    
-   **Features**:
    
    -   **Multiple Stages**: Featuring various characters like a cleaner, farmer, cook, and more.
    -   **Interactive Effects**: Clicking generates rain and drop animations.
    -   **Sound Effects**: Engaging audio enhances the gameplay experience.
    -   **Timed Progression**: Stages change automatically after a set duration.
-   **Technologies**: Pygame.
    
-   **How to Play**:
    
    -   Click anywhere on the screen to create a "rain" effect that reveals parts of the image.
    -   Try to guess the hidden character based on the revealed sections.
    -   Each stage lasts approximately 4 seconds before moving to the next.
-   **Instructions**:
    
    -   Run `2Guess Who I Am.py`.
    -   Make sure all asset files are in the correct locations.
    -   Enjoy the game and see how many characters you can guess.

### 3. Rainfall

-   **Description**: An immersive rain simulation featuring thunder, lightning, and an interactive umbrella. Experience a realistic rainy environment with soothing sounds and responsive visuals.
    
-   **Features**:
    
    -   **Dynamic Raindrops**: Varying sizes, speeds, and transparency for a realistic effect.
    -   **Thunder and Lightning**: Click to trigger lightning flashes and thunder sounds.
    -   **Interactive Umbrella**: Move your mouse to control the umbrella and shield yourself from rain.
    -   **Ambient Soundtrack**: Background rain sounds for a fully immersive experience.
-   **Technologies**: Pygame, Pygame.mixer for audio.
    
-   **How to Play**:
    
    -   Move your mouse to control the umbrella and prevent raindrops from hitting the ground.
    -   Click to trigger lightning and thunder, which also affects the rain intensity.
    -   Watch as raindrops interact with the umbrella.
-   **Instructions**:
    
    -   Run `3Rainfall.py`.
    -   Ensure all images and sound files (`drop.png`, `umbrella.png`, `rainfall.wav`, etc.) are available.
    -   Adjust the window size if needed; the game adapts to screen resizing.

### 4. Let's Draw Together

-   **Description**: A collaborative and creative application where clicking on the canvas splits it into smaller regions, each displaying a random emoji. It's a fun way to create intricate patterns and explore endless possibilities.
    
-   **Features**:
    
    -   **Split Mechanism**: Click to divide regions horizontally or vertically at random.
    -   **Emoji Display**: Each new region reveals a random emoji in a randomly colored background.
    -   **Dynamic Resizing**: The canvas adjusts to window size changes.
    -   **Sound Effects**: Audio feedback enhances the interaction.
-   **Technologies**: Tkinter for GUI, Pygame for sound.
    
-   **How to Play**:
    
    -   Click anywhere on the canvas to split the region into two new regions.
    -   Enjoy the random emojis and colors that appear.
    -   Continue clicking to create more complex patterns.
-   **Instructions**:
    
    -   Run `4Let's Draw Together.py`.
    -   Ensure Pygame and Tkinter are properly installed.
    -   Close the window to exit the application.

### 5. Magic Bubble

-   **Description**: An enchanting game where you create magical bubbles by interacting with an on-screen character. The game combines charming graphics with interactive bubble generation for a delightful and relaxing experience.
    
-   **Features**:
    
    -   **Interactive Wand**: Control a wand with your mouse to create bubbles.
    -   **Diverse Bubbles**: Generates various bubble types with unique animations.
    -   **Character Interaction**: Bubbles are created when the wand interacts with the character.
    -   **Audio Experience**: Background music and bubble pop sounds.
-   **Technologies**: Pygame, Pygame.mixer for audio.
    
-   **How to Play**:
    
    -   Move your mouse to control the wand.
    -   Position the wand near the character to create bubbles.
    -   Enjoy the visual spectacle as bubbles float and fade.
-   **Instructions**:
    
    -   Run `5Magic Bubble.py`.
    -   Ensure all images (e.g., `girl.png`, `bubble.png`) and sound files are in place.
    -   The game window adjusts to your screen resolution.

### 6. Puzzle Game

-   **Description**: A classic 3x3 sliding puzzle where you rearrange tiles to complete an image. Challenge your problem-solving skills and try to solve the puzzle in the fewest moves possible.
    
-   **Features**:
    
    -   **Randomized Puzzles**: Tiles are shuffled randomly each game.
    -   **Step Counter**: Keeps track of the number of moves you've made.
    -   **Intuitive Controls**: Click on tiles adjacent to the empty space to move them.
    -   **Restart Option**: Easily start a new game at any time.
-   **Technologies**: SimpleGUI (via `simpleguitk`), Pygame.mixer for background music.
    
-   **How to Play**:
    
    -   Click on a tile next to the empty space to slide it.
    -   Continue moving tiles to rearrange the image correctly.
    -   Aim to complete the puzzle in the least number of steps.
-   **Instructions**:
    
    -   Run `6Puzzle Game.py`.
    -   Install `simpleguitk` if not already installed (`pip install simpleguitk`).
    -   The puzzle image is loaded from a URL, so an internet connection is required.

### 7. Bury Me with Money

-   **Description**: A fast-paced arcade game where you catch falling coins using a basket. Collect as many coins as you can to achieve the highest score and win the game.
    
-   **Features**:
    
    -   **Mouse-Controlled Basket**: Move the basket left or right to catch coins.
    -   **Random Coin Drops**: Coins fall at varying speeds and positions.
    -   **Score Tracking**: Real-time display of your current score.
    -   **Winning Condition**: Reach a score of 50 to win, with an option to play again.
-   **Technologies**: Pygame, Pygame.mixer for sound effects.
    
-   **How to Play**:
    
    -   Move your mouse to control the basket at the bottom of the screen.
    -   Catch the coins as they fall to increase your score.
    -   Avoid missing coins to keep the game going smoothly.
-   **Instructions**:
    
    -   Run `7Bury Me with Money.py`.
    -   Ensure all images (`Coin.png`, `Basket.png`) and sound files are correctly placed.
    -   The game window matches your screen size for optimal play.

### 8. Make a Cloth Tiger

-   **Description**: An interactive game where you assemble a cloth tiger by dragging and dropping various parts onto the body. It's a creative activity that encourages attention to detail and spatial awareness.
    
-   **Features**:
    
    -   **Drag-and-Drop Interface**: Easily move parts around the screen.
    -   **Multiple Parts**: Includes ears, eyes, nose, mustache, and more.
    -   **Custom Cursor**: Uses a custom mouse cursor for enhanced visuals.
    -   **Save Functionality**: Press `ESC` to save your assembled tiger as an image.
-   **Technologies**: Pygame.
    
-   **How to Play**:
    
    -   Click and drag each part to its correct position on the tiger's body.
    -   Adjust the placement until the tiger looks complete.
    -   Press `ESC` to save your creation.
-   **Instructions**:
    
    -   Run `8Make a Cloth Tiger.py`.
    -   Ensure all necessary image files are available.
    -   The game runs in fullscreen mode for better interaction; press `ESC` to save and exit.

### 9. Russian Roulette

-   **Description**: A suspenseful game simulating a visual version of Russian Roulette. Spin the needle and see where it lands. The game builds tension with animations and sound, culminating in a surprising finale.
    
-   **Features**:
    
    -   **Spinning Needle**: Start and stop the needle with a button.
    -   **Dynamic Animation**: Smooth acceleration and deceleration of the needle.
    -   **Dramatic Effects**: Visual and audio effects enhance the suspense.
    -   **Fullscreen Experience**: Immersive gameplay in fullscreen mode.
-   **Technologies**: Tkinter for GUI, PIL (Pillow) for image manipulation, Pygame for audio.
    
-   **How to Play**:
    
    -   Click "Start" to begin spinning the needle.
    -   Click "Stop" to slow down and eventually stop the needle.
    -   Watch the outcome with accompanying animations and sounds.
-   **Instructions**:
    
    -   Run `9Russian Roulette.py`.
    -   Ensure all image assets and sound files are properly placed.
    -   Press `ESC` to exit fullscreen mode.

### 10. AI Media Reviewer

-   **Description**: An AI-powered application that generates professional reviews and ratings for various media types such as singers, albums, movies, and games. It uses OpenAI's GPT models to produce insightful and human-like critiques.
    
-   **Features**:
    
    -   **User Input**: Enter the name of the media and select its category.
    -   **AI-Generated Reviews**: Provides a rating out of 10 and a detailed review.
    -   **Error Handling**: Fallback responses if the AI service is unavailable.
    -   **Responsive Design**: Visually appealing interface that adapts to different devices.
-   **Technologies**: Flask for web framework, OpenAI API.
    
-   **How to Use**:
    
    -   Navigate to the AI Media Reviewer section through the web interface.
    -   Input the media name and select the appropriate category.
    -   Click "Generate Review" to receive the AI's evaluation.
-   **Instructions**:
    
    -   Run `app.py` and access `http://localhost:5000/reviewer`.
    -   Ensure your OpenAI API key is set up and valid.
    -   An internet connection is required to access the OpenAI API.

### 11. Praise and Roast AI

-   **Description**: An entertaining AI application that first generates a warm, enthusiastic praise for your input, and then follows up with a witty and humorous roast of that praise. It's a fun way to see different AI-generated perspectives.
    
-   **Features**:
    
    -   **Dual Responses**: Provides both a praise and a roast based on your input.
    -   **Interactive Interface**: Built with Streamlit for quick and easy use.
    -   **AI Humor**: Enjoy the creativity and wit of AI-generated content.
-   **Technologies**: Streamlit for web interface, OpenAI API.
    
-   **How to Use**:
    
    -   Run the Streamlit app to launch the web interface.
    -   Enter any text or topic into the input field.
    -   Click "Submit" to receive both the praise and the roast.
-   **Instructions**:
    
    -   Run `streamlit run "11Praise and Roast AI.py"`.
    -   Ensure the OpenAI API key is configured correctly in the script.
    -   Access the application at `http://localhost:8501`.

### 12. Deal With It

Bonus!!! (A little louder than other pygames, be careful!!!)

-   **Description**: A dynamic particle effect application where letters and sounds create an engaging visual and auditory experience. Move your mouse to generate colorful letter particles that interact on the screen.
    
-   **Features**:
    
    -   **Particle Generation**: Letters "G", "I", and "O" appear at the mouse position.
    -   **Colorful Display**: Random colors from a predefined palette.
    -   **Sound Effects**: Each letter corresponds to a unique sound when generated.
    -   **Particle Physics**: Particles move with velocity and fade out over time.
-   **Technologies**: Pygame, Pygame.mixer for audio.
    
-   **How to Play**:
    
    -   Move your mouse around the screen to generate letter particles.
    -   Listen to the associated sounds for each letter.
    -   Enjoy the visual effects as particles drift and disappear.
-   **Instructions**:
    
    -   Run `12Deal with it.py`.
    -   Ensure all sound files (`439012__fourthwoods__kara-g.ogg`, etc.) are in the correct directory.
    -   Close the window to exit the application.

# License

<<<<<<< HEAD
MIT License. The 1 and 12 are inspired by  [Tim Holman](https://github.com/tholman)

----------   here is the thing When I click the screenshot it says Error Fetching Resource
=======
MIT License. The 1 and 12 are inspired by  [Tim Holman](https://github.com/tholman) 

----------

>>>>>>> 1071233d8e959dd2d06c72f0e8900f95ca1609b8
