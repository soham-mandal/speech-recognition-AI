from email.mime import audio
from importlib.resources import path
from socket import timeout
import pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia
import webbrowser
import os
import numpy as np
import pyaudio
import cv2 #pip install opencv-python
import random
from requests import get
import pywhatkit as kit
import smtplib #pip install secure-smtplib
import sys
import pyjokes #pip install pyjokes
import time
import pyautogui#pip install pyautogui
from bs4 import BeautifulSoup
import requests
import PyPDF2 #pip install PyPDF2
#import instaloader
from pywikihow import search_wikihow #pip install pywikihow
from twilio.rest import Client #pip install twilio
import MyAlarm 
import operator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    print(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    strTime = datetime.datetime.now().strftime("%H:%M:%S")   
    speak(f"It is {strTime}")
    
    speak("I am here. Tell me how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.adjust_for_ambient_noise(source,duration=5)
        r.pause_threshold = 1
        audio=r.listen(source)
        #audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    query = query.lower()
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    with open('account_info.text', 'r') as f:
        info = f.read().split()
        my_password = info[4]
    server.login('soham1999mandal@gmail.com','mandal1999soham')
    server.sendmail('soham1999mandal@gmail.com', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e53c8bef61f84839aec293ec352ae4de'
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head=[]
    day=['first', 'second', 'third', 'fourth', 'fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
        print(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    book = open('abc.pdf','rb') #fill out name or mate it automated
    pdfReader = PyPDF2.PdfFileReader(book) 
    pages = pdfReader.numPages
    speak(f'Total number of pages in this book {pages}')
    speak('Which page do yoyu want me to read')
    pg = int(input('Please enterthe page number:'))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def account_info():
    with open('account_info.text', 'r') as f:
        info = f.read().split()
        number = info[0]
        password = info[1]
    return number, password

number, password = account_info()

def TaskExecution():
    #pyautogui.press('esc')
    #speak('verification successful')
    #speak('welcome back')
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #mistake here
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            options = Options()
            options.add_argument('start-maxsized')
            driver = webdriver.Chrome(options=options)

            driver.get('https://www.youtube.com/')

            speak('what do you want me to search in youtube')
            cm = takeCommand().lower()

            search_xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'

            time.sleep(2)
            driver.find_element_by_xpath(search_xpath).send_keys(cm)
            time.sleep(0.5)
            pyautogui.press('enter')
        elif 'open google' in query:
            speak('what do you want me to search in google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'open discord' in query:
            webbrowser.open("www.discord.com")
        elif 'send whatsapp message' in query:
            kit.sendwhatmsg('+919903374564','testing message delivered',2,25) #give no to be sent, must be logged in whatsap web and 2,25 is time which should be atlease 2 min before original time
        elif 'play music' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)    
            #os.startfile(os.path.join(music_dir, random.choice(songs)))
            for s in songs:
                if s.endwith('.mp3'):
                    os.startfile(os.path.join(music_dir, s))
        elif 'open notepad' in query:
            npath = r'C:\Users\Soham\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.exe'
            os.startfile(npath)
        elif 'open telegram' in query:
            tpath = r'C:\Users\Soham\AppData\Roaming\Telegram Desktop\Telegram.exe'
            os.startfile(tpath)
        elif 'open command prompt' in query:
            os.system('start cmd')
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            os.system('start cmd')
            vid = cv2.VideoCapture(0)
  
           # while(True):
           #     ret, frame = vid.read()
           #     cv2.imshow('frame', frame)
           #     if cv2.waitKey(1) & 0xFF == ord('q'):
           #         break
           # vid.release()
           # cv2.destroyAllWindows()
        elif 'open mobile camera' in query:
            import urllib.request
            URL ='http://   /shot.jpg'#enter ip add here, hotspot on and IP Webcam android app
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam',img)
                q=cv2.waitKey(1)
                if q==ord('q'):
                    break
            cv2.destroyAllWindows()

        elif 'alarm' in query:
            speak('Please tell me the time to set alarm. for example, set alarm to 5:30 p.m.')
            tt = takeCommand() #set alarm to 5:30 p.m.
            tt = tt.replace('set alarm to','') #5:30 p.m.
            tt = tt.replace('.','') #5:30 pm
            tt = tt.upper() #5:30 PM
            MyAlarm.alarm(tt)
        
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your ip address is {ip}')
        elif 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences =4)
            speak('according to wikipedia')
            speak(results)
       # elif 'send message' in query:
       #     kit.sendwhatmsg('9163030455','this is testing message',2,25)
        elif 'send email' in query:
            try:
                speak('what should i say')
                content = takeCommand().lower()
                speak('to whom')
                mailid = input('Enter to email here:')
                sendEmail(mailid, content)
                speak('email has been sent')

            except Exception as e:
                print(e)
                speak('sorry, could not send mail')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
      #  elif 'set alarm' in query:
       #     nn = int(datetime.datetime.now().hour)
        #    if nn==22:
         #       music_dir = 'F:\\songs'
          #      songs = os.listdir(music_dir)    
           #     os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)   

        elif 'do some calculations' in query or 'can you calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak('Say something you want me to calculate: example 3 plus 3')
                print('listening....')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add, 
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak('your result is')
            speak(eval_binary_expr(*(my_string.split())))

        elif 'shut down the system' in query:
            os.system('shutdown /s /t 5')
        elif 'restart the system' in query:
            os.system('shutdown /r /t 5') 
        elif 'sleep the system' in query:
            os.system('rundll32.exe powrprof.dll, SetSuspendState 0,1,0') 
        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')  
        elif 'take a screenshot' in query:
            img = pyautogui.screenshot(f'{random.random()}.png')
            img.save(f'{random.random()}.png')
        elif 'open task manager' in query:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('ctrl')
            pyautogui.press('delete')
            time.sleep(1)
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('alt')
        elif 'tell me todays news' in query:
            speak('please wait, fetching the latest news')
            news()
        elif 'read pdf' in query:
            pdf_reader()
        elif 'volume up' in query:
            pyautogui.press('volumeup')
        elif 'volume down' in query:
            pyautogui.press('volumedown')
        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press('volumemute')

        elif 'open facebook' in query:
            options = Options()
            options.add_argument('start-maxsized')
            driver = webdriver.Chrome(options=options)

            driver.get('https://www.facebook.com/login/')

            username_xpath = '//*[@id="email"]'
            password_xpath = '//*[@id="pass"]'
            login_xpath = '//*[@id="loginbutton"]'

            time.sleep(2)

            driver.find_element_by_xpath(username_xpath).send_keys(number)
            time.sleep(0.5)
            driver.find_element_by_xpath(password_xpath).send_keys(password)
            time.sleep(0.5)
            driver.find_element_by_xpath(login_xpath).click()

        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak('please enter the user name correctly')
            name = input('Enter username here:')
            webbrowser.open(f'www.instagram.com/{name}')
            speak(f'Sir here is the profile of the user {name}')
            
        elif 'what is my location' in query:
            speak('wait sir, let me check')
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.getjs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f'I think we are in {city} city in {state} state if country {country}')
            except Exception as e:
                speak('sorry due to network issue I dont know where the hell you are')
                pass

        elif 'weather' in query or 'temperature' in query:
            ipAdd = requests.get('https://api.ipify.org').text
            url = 'https://get.getjs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            url = f'https://www.google.com/search?q=temperature in {city}' #change this with selenium
            r = requests.get(url)
            data = BeautifulSoup(r.text,'html.parser')
            temp = data.find('div', class_='BNeawe').text
            speak(f'current temperature in {city} is {temp}')

        elif 'activate queries' in query:
            speak('query activated tell me what you want to know')
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif 'send message' in query:
            speak('what should I say?')
            msz = takeCommand()

            account_sid = 'ACfa1a56820d6dd756f67724ae90804187'
            auth_token = '77e3dc0e59c797e7f6e2e9edb06c186a'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=msz,
                    from_='+14783752355',
                    to='+919748667832'
                )

            print(message.sid)

        elif 'call me' in query:

            account_sid = 'ACfa1a56820d6dd756f67724ae90804187'
            auth_token = '77e3dc0e59c797e7f6e2e9edb06c186a'
            client = Client(account_sid, auth_token)

            message = client.calls \
                .create(
                    teiml='<Response><Say> Hi whats up, I am Soham, have a terrible day and do not call me again..</Say></Response>',
                    from_='+14783752355',
                    to='+919748667832'
                )

            print(message.sid)


        elif 'no thanks' in query:
            speak('thanks for destroying my time')
            speak('bye-bye')
            sys.exit()
        
        speak('So any more commands ?')


if __name__=="__main__" :
    TaskExecution()