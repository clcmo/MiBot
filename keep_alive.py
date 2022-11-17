from flask import Flask, render_template
from threading import Thread
import webbrowser

app = Flask('')

@app.route('/')
def home():
    return render_template('main.html')

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
