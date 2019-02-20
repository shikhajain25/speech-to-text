# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:47:23 2019

@author: SH20026356
"""
import os
import speech_recognition as sr
from tqdm import tqdm
from multiprocessing.dummy import Pool
import argparse
import base64
import json
from flask import jsonify
#import party

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\Users\sh20026356\Desktop\api_key.json"

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')

pool = Pool(8)
def get_speech_service():
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)
    



def main(speech_file):
    """Transcribe the given audio file.

    Args:
        speech_file: the name of the audio file.
    """
    print("File Recieved")
    with open(speech_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                #'sampleRate': 24000,  # 16 khz
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    response = service_request.execute()
    
    res=json.dumps(response)
    print(res)
    print(type(res))
    return res
    
'''  
if __name__ == '__main__':

    #parser = argparse.ArgumentParser()
    #parser.add_argument(
    #    'speech_file', help='Full path of audio file to be recognized')
    #args = parser.parse_args()
    #main(args.speech_file)

   
    print("please speak a word into the microphone")
    party.record_to_file('demo1.wav')
    print("done - result written to demo.wav")
    speech_file = 'demo1.wav'
    print(speech_file)
    print("done - result written to demo.wav")
    main(speech_file)
    
'''
