# iris-battleship
Why not a game in contest?

## Have you ever played Battleship?

Battleship is a guessing game for 2 players.

![picture](https://raw.githubusercontent.com/renatobanzai/iris-battleship/main/img/battleship_game.jpg)

## You can try here:
http://iris-battleship.eastus.cloudapp.azure.com/new

## Screenshot
![picture](https://raw.githubusercontent.com/renatobanzai/iris-battleship/main/img/iris_battleship_arrange.gif)

## Rules
To be played by 2 people. On first screen we have a URL that should be sent to the another player. After sending 
this URL, you can click on the link to arrange your ships on the map. Finished arranging you just click on save link and 
start guessing. The upper map is where you can click / touch the map to try drown your enemy's ships. On the lower map 
you can follow how your enemy is shooting you.  

## Architecture
I made the frontend using HTML5 + Javascript, and to connect to Iris I use python + IRIS Native API. 

## How to run in your own machine
### Prerequisites
* git
* docker and docker-compose
* access to a terminal in your environment

### Installing
After cloning this repo open a terminal go to the iris-battleship folder and type these commands:

```
git clone https://github.com/renatobanzai/iris-battleship
```

### Running in linux and MacOS
```
docker-compose build

docker-compose up
```

After this, go to the address:

http://localhost/new




