import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import pyjokes
from GoogleNews import GoogleNews

warnings.filterwarnings('ignore')

def recAudio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Something')
        audio = r.listen(source)


    data = ''
    try:
        data = r.recognize_google(audio)
        print ('You said: '+ data)

    except sr.UnknownValueError:
        print('Something Went wrong,try again')
    except sr.RequestError as e:
        print('Check ur Connection '+ e) 

    return data

def assistantResponse(text):
    print(text)

    myobj = gTTS(text= text, lang='en', slow=False)
    myobj.save('response.mp3')
    os.system('start response.mp3')

def WakeWord(text):
    WAKE_WORDS = ('hey electric', 'okay electric', 'electric')
    text=text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names =  ['January', 'February', 'March', ' April', 'May', 'June', 'July','August', 'September', ' October', 'November', 'December']

    ordinalNumbers = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', 
    '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return 'It is '+weekday+' '+ordinalNumbers[dayNum-1]+' of '+month_names[monthNum-1]+'. '

def greeting(text):
    GREETING_INPUTS = {'hi', 'hey', 'hello', 'hello there', 'hi there', 'hola', 'nigga'}
    GREETING_RESPONSES = {'hello there!', 'Hi! Such a lovely day', 'Hello iam here for ur help', 'Hola'}

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) +'.'

    return ''


def getPerson(text):

    wordList = text.split()

    for i in range(0, len(wordList)):
        if i+3 <= len(wordList)-1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+ wordList[i+3]

while True:

    text = recAudio()
    response = ''            
    
    if(WakeWord(text) == True):
        response = response + greeting(text)

        if ('date' in text):
            get_date = getDate()
            response = response + '' + get_date

        if ('time' in text):
            now = datetime.datetime.now()
            midday = ''
            if now.hour >= 12:
                midday = 'PM'
                hour = now.hour - 12
            else:
                midday = 'AM'
                hour = now.hour

            if now.minute < 10:
                minute = '0' + str(now.minute)        
            else:
                minute = str(now.minute)

            response = response + ' ' +str(now.hour)+ ':'+ minute + ' '+midday        
    
        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            response = response + '' + wiki

        if ('LOL XD' in text):
            meme = 'Mat maan Ma Chuda'
            response = response + '' + meme   

        if ('joke' in text):
            joke = pyjokes.get_joke()
            response = response + '' + joke

            

        assistantResponse(response)
                      


      