from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('lmX3MVZvZvyPRe9HOQ0FIKBExa00OnHF7wjXkuOlEB1s')
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

def get_eng_to_french(eng_text):
    """converts eng text to french"""
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/4a724eb9-4a24-4e85-8ec9-1f8057ad15fa')
    translation = language_translator.translate(
    text=eng_text,
    model_id='en-fr').get_result()
    ret=translation['translations'][0]['translation']
    return ret



def get_fr_to_english(fr_text):
    """converts french text into english"""
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/4a724eb9-4a24-4e85-8ec9-1f8057ad15fa')
    translation = language_translator.translate(
    text=fr_text,
    model_id='fr-en').get_result()
    ret=translation['translations'][0]['translation']
    return ret
