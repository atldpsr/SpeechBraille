from ibm_watson import SpeechToTextV1
from os.path import join, dirname
import json

data = ''
speech_to_text = SpeechToTextV1(
    iam_apikey='L1P_UXHvVeeEmQFXn-4_SqnMPDT3GO5_4iHHULs9_pVn',
    url='https://gateway-lon.watsonplatform.net/speech-to-text/api'
)

def recognize(filename):
    with open(join(dirname(__file__), './.', filename), 'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            word_alternatives_threshold=0.9,
        ).get_result()
    print(json.dumps(speech_recognition_results, indent=2))
    try:    
        sentence = speech_recognition_results['results'][0]['alternatives'][0]['transcript']
    except KeyError:
        sentence = ''        
        print(json.dumps(speech_recognition_results, indent=2))
    return sentence
        

