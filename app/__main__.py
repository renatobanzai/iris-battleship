from flask import Flask, render_template, request
from iris_python_suite import irisdomestic
import yaml

#todo: demonstrate a profile of different aproachs in code
try:
    with open("../data/config.yaml", "r") as file:
        config = yaml.safe_load(file)
except Exception as e:
    print('Error reading the config file')

#Class with IRIS Persistence
obj_irisdomestic = irisdomestic(config["iris"])

app = Flask(__name__)
@app.route('/new')
def new():
    if obj_irisdomestic.isDefined("maxgame"):
        max = int(obj_irisdomestic.get("maxgame"))+1
    else:
        max = 1

    obj_irisdomestic.set(max, "maxgame")

    return render_template('new.html', game_id=max)

@app.route('/arrange/p1/')
def arrangep1():
    game_id = request.args.get('game_id')
    return render_template('test2.html', player="p1", game_id=game_id)

@app.route('/arrange/p2/')
def arrangep2():
    game_id = request.args.get('game_id')
    return render_template('test2.html', player="p2", game_id=game_id)

@app.route('/save/')
def save():
    game_id = request.args.get('game_id')
    player = request.args.get('player')
    ships = request.args.get('ships')
    obj_irisdomestic.set(ships, game_id, player, "ships")
    return render_template('game.html', game_id=game_id, player=player)

@app.route('/caniplay/')
def CanIPlay():
    result = "0"
    game_id = request.args.get('game_id')
    player_id = request.args.get('player')
    if(obj_irisdomestic.isDefined(game_id, "lastplayer")==False
            and obj_irisdomestic.isDefined(game_id, "p1", "ships")
            and obj_irisdomestic.isDefined(game_id, "p2", "ships")):
        if player_id == "p1":
            result="1"
    else:
        if player_id != obj_irisdomestic.get(game_id, "lastplayer"):
            result="1"

    return result


@app.route('/xplode/')
def xplode():
    opponent = {"p1": "p2", "p2": "p1"}
    game_id = request.args.get('game_id')
    player = request.args.get('player')
    target = request.args.get('target')

    ships = obj_irisdomestic.get(game_id, opponent[player], "ships")
    if ships.find(target) > -1:
        result = "hit"
    else:
        result = "miss"

    obj_irisdomestic.set(player, game_id, "lastplayer")

    return result


app.run(host="0.0.0.0")