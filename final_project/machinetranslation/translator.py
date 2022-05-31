"""Import files"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION='2018-05-01'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    This function takes the english text and returns it in french
    """
    if english_text == '':
        return ''

    translation_object = language_translator.translate(text=english_text, model_id='en-fr')
    translation = translation_object.get_result()
    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """
    This function takes the french text and returns it in english
    """
    if french_text == '':
        return ''

    translation_object = language_translator.translate(text=french_text, model_id='fr-en')
    translation = translation_object.get_result()
    english_text = translation['translations'][0]['translation']

    return english_text
