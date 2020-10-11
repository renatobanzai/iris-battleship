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
    player_id = request.args.get('player')
    ships = request.args.get('ships')
    obj_irisdomestic.set(ships, game_id, player_id, "ships")
    return render_template('game.html')


app.run(host="0.0.0.0")