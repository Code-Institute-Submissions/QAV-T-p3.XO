# Tic-Tac-Toe Game

## Index

1. [Purpose of the Project](#purpose-of-the-project)
2. [User Stories](#user-stories)
3. [Features](#features)
4. [Future Features](#future-features)
5. [Technology](#technology)
6. [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Manual Testing](#manual-testing)
7. [Fixed Bugs](#fixed-bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Purpose of the Project

The purpose of this project is to create a simple command-line Tic-Tac-Toe game where two players can compete against each other.

## User Stories

- As a player, I want to be able to see the game board displayed clearly.
- As a player, I want to take turns playing X and O.
- As a player, I want the game to end when someone wins or it's a tie.
- As a player, I want the option to play again after the game ends.
- As a player, I want the option to quit the game at any time.

## Features

- Display the game board.
- Alternate turns between players X and O.
- Check for a win or tie after each turn.
- Allow players to play again or quit.

## Future Features

- Implement an AI opponent for single-player mode.
- Add a graphical user interface (GUI) for a more interactive experience.
- Implement a scoring system to keep track of wins, losses, and ties.

## Technology

- Python 3
- OS module for clearing the screen
- Markdown for README formatting

## Testing

### Code Validation

The code has been validated using Python's PEP 8 style guide and linted for syntax errors.

### Manual Testing

**Test 1:** Launch the game.
- Run the Python script run.py.
- Verify that the game starts and displays the initial game board.

**Test 2:** Input invalid spots to check for proper error handling.
- Enter a non-numeric character as input during the game.
Confirm: The game should display an error message and prompt the user to enter a valid spot.
- Enter a number outside the range of 1-9 as input.
Confirm: The game should display an error message and prompt the user to enter a valid spot.
- Choose a spot that is already taken.
Confirm: The game should display an error message and prompt the user to enter a valid spot.
- Enter a number outside the range of 1-9 as input.
Confirm: The game should display an error message and prompt the user to enter a valid spot.

**Test 3:** Play a game to completion, ensuring win and tie conditions are detected correctly.
- Take turns playing the game until someone wins.
Confirm: The game should detect the winning condition and declare the winner.
- Play the game until all spots are filled and no one wins.
Confirm: The game should detect the tie condition and declare it's a tie.
- Choose to play again after the game ends.
Confirm: The game should reset and start a new game.
- Choose to quit the game at any time.
Confirm: The game should exit.

## Fixed Bugs

- Corrected a bug where the wrong player was declared the winner.
- Fixed an issue where player X and O were incorrectly assigned in the game logic.

## Deployment

This project is deployed using the Code Institute template and hosted on Heroku.com. To deploy the project, follow these steps:

**Clone the Repository:**
- Clone this repository to your local machine using the following command:
bash
Copy code
git clone https://github.com/your-username/your-repository.git
Replace your-username with your GitHub username and your-repository with the name of your repository.
**Install Dependencies:**
- Navigate to the project directory and install the required dependencies using the following command:
Copy code
pip install -r requirements.txt
**Configure Heroku:**
- Log in to your Heroku account or create a new one at Heroku.com.
- Create a new Heroku app by clicking on the "New" button and following the prompts.
**Deploy the App:**
- Once the Heroku app is created, navigate to the "Deploy" tab.
- Choose the deployment method (GitHub, GitLab, Bitbucket) and connect your repository.
- Choose the branch you want to deploy and click on "Deploy Branch".
**Set Environment Variables:**
- If your project requires any environment variables, navigate to the "Settings" tab on Heroku.
- Click on "Reveal Config Vars" and set your environment variables.
**Open the App:**
- Once the deployment is complete, click on the "Open App" button to view your deployed project.

## Credits
Looked over few sources that I credit

https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode
https://www.youtube.com/watch?v=Q6CCdCBVypg
https://www.youtube.com/watch?v=Q6CCdCBVypg
