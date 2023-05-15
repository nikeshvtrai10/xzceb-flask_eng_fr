'''Translator'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#authenticate
authenticator = IAMAuthenticator(apikey)

#setup service
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Converts English to French'''
    french_translation = language_translator.translate(text=english_text,\
        model_id='en-fr').get_result()
    return french_translation['translations'][0]['translation']

french = english_to_french("I am a Software Engineer.")
print(f"The french translation is : {french}")

def french_to_english(french_text):
    '''Converts French to English'''
    #write the code here
    english_translation = language_translator.translate(text=french_text,\
        model_id='fr-en').get_result()
    return english_translation['translations'][0]['translation']

english = french_to_english("Je suis ingénieur logiciel.")
print(f"The english translation is : {english}")
