import os
import api
import requests
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import asyncio
import speech_recognition as sr

import nest_asyncio
nest_asyncio.apply()
token="xoxb-101944332577-698195991045-QpfdLEMbpRI3oaSnp8DN6ks3"
agent = Agent.load("models/depot", interpreter=RasaNLUInterpreter("models/depot/nlu"))

client = api.WebClient(
    token=token,
    run_async=True
    )
def sendMsg(msg,channel):
   event_loop = asyncio.get_event_loop()  
   response = event_loop.run_until_complete(client.chat_postMessage(
        channel=channel,
        text=msg
        )
    )
def response(txt):
   event_loop = asyncio.get_event_loop()  
   result = event_loop.run_until_complete(agent.handle_text(txt,None,None,"jesenchen"))
   client.chat_postMessage(
        channel='#general',
        text=result[0]["text"]
        )

def downloadFile(url):
    print("download from %s" % url)
    headers = {"Authorization":"Bearer xoxb-101944332577-698195991045-QpfdLEMbpRI3oaSnp8DN6ks3"}
    local_filename = url.split('/')[-1]
    doc = requests.get(url,headers=headers) 
    with open(local_filename, 'wb') as f:
	    f.write(doc.content)
	    f.close()
	
    r = sr.Recognizer()
    recordfy = sr.AudioFile('recordfy.wav')
    with recordfy as source:
        audio = r.record(source)
    result = r.recognize_google(audio)
    

    return response(result)



@api.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    print(data)
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if not data['files'] is None:   
        files = data["files"]
        file = files[0]["url_private_download"]
        result = downloadFile(file)
        


slack_token = "xoxb-101944332577-698195991045-QpfdLEMbpRI3oaSnp8DN6ks3"
rtm_client = api.RTMClient(token=slack_token)
rtm_client.start()

