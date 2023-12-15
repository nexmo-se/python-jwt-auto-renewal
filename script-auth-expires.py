#!/usr/bin/env python3
import os

import vonage

from dotenv import load_dotenv
load_dotenv()

import threading
interval = 240 # repeat timer in seconds

import datetime

#---

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")

VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.getenv("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

FROM_NUMBER = os.getenv("FROM_NUMBER")

TO_NUMBER = os.getenv("TO_NUMBER")

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

#---

def periodicCall():

  print(datetime.datetime.now())

  response = client.voice.create_call({
    'to': [{'type': 'phone', 'number': TO_NUMBER}],
    'from': {'type': 'phone', 'number': FROM_NUMBER},
    'ncco': [{
      'action': 'talk',    
      'text': 'You are listening to a test text-to-speech call made with the Vonage Voice API',
      'language': 'en-US',
      'style': 0
    }]
  })

  print(response)

#---

def startCallTimer():
    
    threading.Timer(interval, startCallTimer).start()
    periodicCall()

#---

startCallTimer()





