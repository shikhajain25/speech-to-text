# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 08:46:20 2019

@author: SH20026356
"""

from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask_restful.utils import cors

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5600)