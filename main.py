from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

apikey = 'YOUR API KEY'
url = 'YOUR URL'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

voices = tts.list_voices().get_result()
print(json.dumps(voices, indent=2))

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello World! Its Marseille baby', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

with open('drake.txt', 'r') as f:
    text = f.readlines()
    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)
    
with open('./drake.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)

with open ("freeze.txt", 'r') as f:
    text = f.readlines()
    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)

voice = 'fr-FR_ReneeVoice'

with open('./freeze.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice=voice).get_result()
    audio_file.write(res.content)
