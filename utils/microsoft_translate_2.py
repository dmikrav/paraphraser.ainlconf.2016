# coding: utf-8
import websocket
import thread
import json
import requests
import urllib
import wave
import audioop
from time import sleep
import StringIO
import struct
import sys
import codecs
from xml.etree import ElementTree


doItAgain = "yes" #Control While loop


def GetToken(): #Get the access token from ADM, token is good for 10 minutes
    urlArgs = {
        'client_id': '7653b7a7-3e8e-417c-ad75-5208e2e88eef',
        'client_secret': 'gL3n1fVtn4U5lLRTg0j+PKoSGSMM7/Tq19fGJZtiQxk',
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }

    oauthUrl = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'

    try:
        oauthToken = json.loads(requests.post(oauthUrl, data = urllib.urlencode(urlArgs)).content) #make call to get ADM token and parse json
        finalToken = "Bearer " + oauthToken['access_token'] #prepare the token
    except OSError:
        pass

    return finalToken
#End GetToken

finalToken = GetToken() 

def GetTextAndTranslate(textToTranslate):
    #Call to Microsoft Translator Service
    textToTranslate = "Привет всем"
    toLangCode = "en"
    headers = {"Authorization ": finalToken}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)
   
    try:
        translationData = requests.get(translateUrl, headers = headers) #make request
        translation = ElementTree.fromstring(translationData.text.encode('utf-8')) # parse xml return values
        print translation.text #display translation

    except OSError:
        pass

    print " "
#End GetTextAndTranslate()

GetTextAndTranslate(finalToken)

