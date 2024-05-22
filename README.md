# FreeVideoGameFiner

## Project Description and Features

This is an application for gaming enthusiasts looking for free PC games.

Targeted primarily at gamers seeking cost-free gaming options, this application simplifies discovering new and exciting games.

1. Users can find a randomly selected game from the homepage

2. Conduct specific game searches, yielding detailed information, including descriptions, platform availability, genres...

3. the application lets users browse the entire collection of free PC games

4. Users can refine search based on specific genres and developers
  
Overall, this application is not just a gateway to free games but also an intuitive tool that caters to the diverse preferences of gaming aficionados, ensuring they find exactly what they're looking for with ease and convenience.


## Environment Setup

#### Getting Started
- Steamlit will need to be installed to run the application.

#### Prerequisites
- Before you begin, ensure you have the following installed:

```sh
Streamlit: pip3 install streamlit
```

#### Usage:

This Streamlit application is the front-end for users to access and explore  various free-to-play PC games. It allows users to randomly discover games, search for games by title, and browse a list of games with options to filter and sort.

## Run the app

####  Through URL
- Access the application through the following URL:
```sh
https://freevideogamefinder.streamlit.app/
```

#### Through Terminal
- After setting up the enviroment 
	1. Clone the repository:
	2. Navigate to the project directory
	3. Install the required packages
	4. Run the Streamlit app
```sh
# Step 1:
git clone https://github.com/your-username/FreeVideoGameFiner.git

#step 2:
cd .../FreeVideoGameFinder

#step 3:
pip install -r requirements.txt

#step 4:
streamlit run free_game_app.py

```

## API Used

### API description: Free-To-Play Games Database API

- API document: https://www.freetogame.com/api-doc

- API with endpoint: https://www.freetogame.com/api/games?platform=pc


## Page interaction description:

### Home Page:
- **Welcome Message**: greets the user.

- **Random Game Selection**: A button selects and displays a random game when clicked.

- **Displaying Game Details**:Engage users in discovering free

- **Another random game**: Allow user todo multiple clicks to display different random games.
  

### Search Game page:


- **User input**: A text box to search games with the title.

- **Game Title Search**: Display the game details according to the input.

- **Search result display**: Lists matching games with details, shows all games if no input, and displays an error if no matches are found.
  

### Explore All Games page:

  
**Feature:**

- Display all games: All the games are laid out for users to browse.

- Sort by time: Allows user to sort all games based on release dates.

- Filter by genre: Enables filtering games by genre, helping users find games that match their interests.



## Next steps:

- **Implementing a User Class**: Create a user class allowing a login function. The class will manage user profiles and interactions, like saving favorite games and managing a personalized game list, and it also allows a thumbs-up button.
- **Thumbs-Up Feature**: Implement the thumbs-up functionality within the Game class, allowing users to like games. Also, it should save the thumbs-up record in the session state and user class, which allows each user to like only a game once.


