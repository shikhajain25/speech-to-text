# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:14:11 2019

@author: SH20026356
"""

import complete
import party
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class stt(Resource):
    def get(self):
        print("please speak a word into the microphone")
        party.record_to_file('demo1.wav')
        #print("done - result written to demo.wav")
        speech_file = 'demo1.wav'
        print(speech_file)
        print("done - result written to demo.wav")
        #result = complete.main(speech_file)
        #print(result)
        result = "HI,this is shikha"
        print(result)
        return result

api.add_resource(stt, "/stt")

if __name__ == '__main__':
     app.run(debug = True)