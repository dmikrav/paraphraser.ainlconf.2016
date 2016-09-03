# coding : utf-8
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


def GetTextAndTranslate(finalToken):

    fromLangCode = " "
    toLangCode = " "
    textToTranslate = " "

    print " "
    print "   Language List"
    print "     English"
    print "     German"
    print "     Italian"
    print "     Spanish"
    print "     French"

    #Get the source Language
    while (fromLangCode == " "):
        sourceLang = raw_input("Type the name of a language from the list that you want to translate from: ")

        if (sourceLang == "english") or (sourceLang == "English"):
            fromLangCode = "en"
        elif (sourceLang == "German") or (sourceLang == "german"):
            fromLangCode = "de"
        elif (sourceLang == "Italian") or (sourceLang == "italian"):
            fromLangCode = "it"
        elif (sourceLang == "Spanish") or (sourceLang == "spanish"):
            fromLangCode = "es"
        elif (sourceLang == "French") or (sourceLang == "french"):
            fromLangCode = "fr"
        else:
            print " "
            print "You need to pick a language from the List"

            error = raw_input("Press any key to continue")

    #End while
    
    print " "

    #Get the desitination Language
    while (toLangCode == " "):
        destLang = raw_input("Type the name of a language from the list that you want to translate to: ")

        if (destLang == "english") or (destLang == "English"):
            toLangCode = "en"
        elif (destLang == "German") or (destLang == "german"):
            toLangCode = "de"
        elif (destLang == "Italian") or (destLang == "italian"):
            toLangCode = "it"
        elif (destLang == "Spanish") or (destLang == "spanish"):
            toLangCode = "es"
        elif (destLang == "French") or (destLang == "french"):
            toLangCode = "fr"
        else:
            print " "
            print "You need to pick a language from the List"

            error = raw_input("Press any key to continue")

    #End while
    
    print " "

    textToTranslate = raw_input("Type the text that you want to translate:  ")

    print " "

    #Call to Microsoft Translator Service
    headers = {"Authorization ": finalToken}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)
   
    try:
        translationData = requests.get(translateUrl, headers = headers) #make request
        translation = ElementTree.fromstring(translationData.text.encode('utf-8')) # parse xml return values
        print "The translation is---> ", translation.text #display translation

    except OSError:
        pass

    print " "
 
#End GetTextAndTranslate()


if __name__ == "__main__":
    
    finalToken = GetToken()

    while (doItAgain == 'yes') or (doItAgain == 'Yes'):
        GetTextAndTranslate(finalToken)
        print ' '
        doItAgain = raw_input('Type yes to translate more, any other key to end: ')
    #end while
        
    goodBye = raw_input('Thank you for using Microsoft Translator, we appreciate it. Good Bye')

#end main
