# Software Requirements

## Vision

CodeFighter is a "best 2-out-of-3" style fighting game where opponents will battle in a 3-round fight. Our vision is to create an entertaining multiplayer experience to allow users to battle online. It solves the pain point of ever-present boredom, and what better way than to play a game with someone else! Our product provides an opportunity for social interaction in a socially-distant world. 

## Scope

**In**:

* User can move character on screen
* User can see opponent’s name, and opponent’s character moving on screen
* User can see their score
* User’s character can collide with the opponent’s character
* Application can connect via socket.io
* *Stretch goal:* Application can write CRUD operations

**Out**:

* Application won't allow more than 2 players per game
* Application won't be web-based
* Application won't be a social media platform

### MVP

Our minimum-viable product is a real-time, two player game.

### Stretch Goals

* Adding a database to keep track of player's past scores and high scores
* Additional levels/fight scenes
* Create a script to allow users to download game package

## Functional Requirements

* User can start a game and wait inside a lobby
* 2nd user can join lobby
* Provide a "start" button once two players are present
* Open game window
* Players collide, damage is done, points amass, a winner is declared.

### Data Flow

1. Initialize game
2. Initialize two "player" instances
3. Players have health properties to determine end of round
4. Players' "score" property is implemented
5. When a player runs out of health, they lose. Their opponent is awarded points.
6. After 3 rounds, players are offered options to "play again" or "exit to lobby"
7. "Play again" restarts new 3-round game
8. "Exit to lobby" returns players to lobby 

## Non-Functional Requirements

Security is important, we don’t want to send any user’s personal information in our app.
We want 80% code coverage with our testing to ensure we’re examining not just what we expect to happen DOES happen, but to find the edge cases as well.
Reliability is a cornerstone of our app - if the user can’t play a game reliably, they’ll stop using our product.
