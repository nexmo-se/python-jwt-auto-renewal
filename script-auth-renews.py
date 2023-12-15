#!/usr/bin/env python3
import os

import vonage

from dotenv import load_dotenv
load_dotenv()

#===== Add this section to your actual Python code =====

import datetime

import threading
authDuration = 960 # Auth validity duration after renewal - 16 minutes (960 seconds)
authInterval = 900 # Auth renewal timer - 15 minutes (840 seconds)

#================== End add section =====================

callInterval = 240 # repeat call timer in seconds - JUST FOR DEMO

#---

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")

VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.getenv("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

FROM_NUMBER = os.getenv("FROM_NUMBER")

TO_NUMBER = os.getenv("TO_NUMBER")

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

#===== Add this section to your actual Python code =====

def periodicAuthRenew():

  exp = int(datetime.datetime.now().timestamp())

  client.auth(exp = exp + authDuration)

  print(datetime.datetime.now(), 'Auth renewed\n')

#---

def startAuthTimer():
    
  threading.Timer(authInterval, startAuthTimer).start()
  periodicAuthRenew()

#---

startAuthTimer()

#================== End add section =====================


#-- the following till end of this program is for only to demo the above Auth renewal is working as expected
#-- wait at least 16+ min after program launch to see that new API requests after that are working

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

  print(response, '\n')

#---

def startCallTimer():
    
  threading.Timer(callInterval, startCallTimer).start()
  periodicCall()

#---

startCallTimer()





