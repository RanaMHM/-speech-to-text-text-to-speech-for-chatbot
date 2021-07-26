# Documentation: https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices
#pip install ibm_watson

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'HmSzNLfXzeOmXNoiAWLj-DEmqsvB1z75UzvojcGc3VYS'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/75defce6-bb6f-4c64-8f46-a165c8db541a'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('./sound.mp3', 'wb') as audio_file:
    res = tts.synthesize(" ,Text-to-speech converted successfully, good job", 
    accept='audio/mp3',voice="en-US_EmilyV3Voice").get_result()
    audio_file.write(res.content)
