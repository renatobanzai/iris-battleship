from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('test2.html')


app.run(host="0.0.0.0")