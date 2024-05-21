# FreeVideoGameFiner

## Project Description
This is an application for gaming enthusiasts looking for free PC games. 
Targeted primarily at gamers seeking cost-free gaming options, 
this application simplifies discovering new and exciting games. 
 
1. Users can find a randomly selected game from the homepage
2. Conduct specific game searches, yielding detailed information, including descriptions, platform availability, genres...
3. the application lets users browse the entire collection of free PC games
4. Users can refine search based on specific genres and developers


Overall, this application is not just a gateway to free games but also an intuitive tool that caters 
to the diverse preferences of gaming aficionados, ensuring they find exactly what they're looking 
for with ease and convenience.
---
## API Used
### API description: Free-To-Play Games Database API
- API document: https://www.freetogame.com/api-doc 
- API with endpoint: https://www.freetogame.com/api/games?platform=pc
---
## Page interaction description: 

There are 3 pages for the application, including the Home page, the Search Game page, and 
the Explore All Games page. All the pages are using the same API endpoint.  
 
- A sidebar is shown on all pages to allow users to navigate the three available pages.  

### Home Page:  
- This page is a welcome page. The page contains a welcome message which greets the user.  
 
#### Features: 
- Random Game Selection: The main page also features a button that, when clicked, 
selects and displays a random game.  
- Displaying Game Details: This feature is designed to engage users in discovering free 
PC games and having more fun using the app. The game and all game details will be 
shown.  
- Another random game: If the user wants another random game, click the button again, 
and another game will be shown. 

### Search Game page: 
- This page lets users input and search for games by game title through the input box.  
#### Feature: 
- User input: A text box that allows users to input any word or letters they want to search 
for games with the title containing the input.  
- Game Title Search: After the button is clicked, any game with the corresponding word 
or letter will show up with the game details. 
- Search result display: Matching games are listed with their details. If nothing is 
entered, all games will be shown. An error message is displayed if no matches are 
found, guiding the user accordingly. 


### Explore All Games page: 
- Users can view a list of all available games, providing an overview of all game options. 
#### Feature:
- Display all games: All the games are laid out for users to browse.  
- Sort by time: The user can sort all games based on release dates.  
- Filter by genre: Users can filter games by genre. Those two customizations allow users 
to find games that align with their interests.  

 ---
## List of classes and objects: 
 
1. Game Class 
   - The Game class represents individual games that include game details. 
 
   - Attributes: 
     - title: The title of the game. 
     - thumbnail: A URL or a path to the game's thumbnail image. 
     - short_description: A brief description of the game. 
     - game_url: The URL to the game's webpage or resource. 
     - genre: The genre category of the game. 
     - developer: The developer of the game. 
     - release_date: The date when the game was released. 
     - thumbs_up_count: The number of 'thumbs-ups' or likes the game has received. 
     - has_thumbs_up: A boolean indicating whether the game has received a thumbs-up. 
 
   - Methods (Those methods have been added to the class but not implemented): 
     - add_thumbs_up(): Increases the thumbs_up_count by one. It is designed to allow users 
     to like a game, and each game will be allowed once per user, which will need a user 
     class. 
 
   - Usage: 
     - This class creates objects that store and represent data fetched from the API about games. 
 
 
2. GameList Class(This is not the best case, but there needs to be more time to reflect. If there 
is more time, a user class will be implemented for game collection and game thumbs up.) 
   - The GameList class manages a collection of Game objects.  
 
   - Attributes: 
     - games: A list that holds instances of the Game class. 
 
   - Methods:
     - load_data(data): Takes game data, which will be using cleaned data from the 
     clean_games_data function, and creates the games of Game objects. 
     - select_random_game(): Randomly selects and returns a game from the games list. 
     - search_by_title(title): Returns a list of games whose titles match the given string. 
     - filter_by_genre(genre): Returns a list of games that match the specified genre. 
 
   - Usage: 
     - This class will manage a collection of games, retrieve random games, and search and filter 
     games. 
---
## Environment Setup
#### Getting Started 
- Steamlit will need to be installed to run the application. 
- The package “random” will be needed. 
 
#### Prerequisites
Before you begin, ensure you have the following installed:
```sh
Streamlit: pip3 install streamlit 
```
Usage:  

This Streamlit application is the front-end for users to access and explore various free-to-play 
PC games. It allows users to randomly discover games, search for games by title, and browse a 
list of games with options to filter and sort.
---
## Next steps: 
- Implementing a User Class: Create a user class allowing a login function.  The class will 
manage user profiles and interactions, like saving favorite games and managing a 
personalized game list, and it also allows a thumbs-up button. 
 
- Thumbs-Up Feature: Implement the thumbs-up functionality within the Game class, 
allowing users to like games. Also, it should save the thumbs-up record in the session 
state and user class, which allows each user to like only a game once. 
  - The method has already been added to the class Game. (add_thumbs_up)