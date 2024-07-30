from flask import Flask,render_template

app = Flask(__name__) #    https://www.youtube.com/watch?v=4dkNn93DIx4 creating an app

import config #meaning config.py

import models

import api

import routes

#orders of the import files must be same

if __name__== '__main__':
    app.run(debug=True)
