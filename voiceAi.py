import speech_recognition as sr
import webbrowser
import pyttsx3 
import requests
from jokes import jokes
import random
import datetime
import os
from gtts import gTTS 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mailId
import subprocess
import ctypes
import winshell
from openai import OpenAI
import pywhatkit
import platform
import cpuinfo
import psutil
import cv2
from datetime import datetime
import phoneNumber
import pyautogui


weather_api = "your_weather_api"
newsapi = "your_news_api"
MyApi="your_openai_api"

def aiProcess(command) :

    client = OpenAI(
        api_key=MyApi,
        base_url="https://api.aimlapi.com",
    )

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant who knows everything.",
            },
            {
                "role": "user",
                "content": f"{command}"
            },
        ],
    )

    message = response.choices[0].message.content
    return message

def get_weather(city):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    url = f'{base_url}?key={weather_api}&q={city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        print(f"Weather in {location}:")
        speak(f"Weather in {location}:")
        print(f"Temperature: {temp_c}°C")
        speak(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")
        speak(f"Condition: {condition}")
    else:
        speak(f"Error fetching weather data: {response.status_code}")



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if c.lower() == "open google":
        speak("opening google....")
        webbrowser.open("https://google.com")

    elif c.lower() == "open facebook":
        speak("opening facebook....")
        webbrowser.open("https://facebook.com")

    elif c.lower() == "open youtube":
        speak("opening youtube....")
        webbrowser.open("https://youtube.com")

    elif c.lower() == "open linkedin":
        speak("opening Linkedin.......")
        webbrowser.open("https://linkedin.com")

    elif c.lower() == "open github":
        speak("opening github.......")
        webbrowser.open("https://github.com")

    elif c.lower() == "open wikipedia":
        speak("opening wikipedia....")
        webbrowser.open("https://wikipedia.com")

    elif c.lower() == "open whatsapp":
        speak("opening whatsapp....")
        webbrowser.open("https://web.whatsapp.com/")

    elif c.lower() == "open instagram":
        speak("opening instagram....")
        webbrowser.open("https://www.instagram.com/")


    elif c.lower().startswith("play") :
        song = c.lower().replace("play ", "")
        speak(f"playing {song}...")
        pywhatkit.playonyt(song)


    elif c.lower() == "tell me a news":
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                for article in articles[:5]:
                    speak(article['title'])
            else:
                speak("Sorry, I could not find any news.")
        else:
            speak("Sorry, I couldn't fetch the news right now.")


    elif c.lower() == "jokes":
        speak("here is your joke :- ")
        joke = random.choice(jokes)
        speak(joke)


    elif c.lower() == "stop assistant":
        speak("thank you sir for spending a little bit time with me...see you next time sir")
        exit()

    elif c.lower() == "what is the time":
        time = datetime.datetime.now().time()
        formatted_time = time.strftime("%H:%M:%S")
        speak(f"sir time is {formatted_time}")


    elif c.lower().startswith("send email"):
        r = sr.Recognizer()
        try:
            emails_send = c.lower().split("send email to ")[1].strip()
            speak(f"sending email to {emails_send}")
            to = mailId.emails.get(emails_send)
            if to:
                speak("What should I say?")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    content = r.recognize_google(audio)
                speak(f"email sending to {to}")
                sendEmail(to, content)
                speak("Email has been sent!")
            else:
                speak(f"Sorry, I don't have an email address for {emails_send}.")
        except IndexError:
            speak("Sorry, I couldn't understand the recipient's name. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Could you please repeat?")
        except sr.RequestError as e:
            speak("Sorry, there was an error with the speech recognition service.")
            print(f"Speech recognition error: {e}")
        except Exception as e:
            speak("Sorry, there was an error sending the email.")
            print(f"Error: {e}") 

    elif c.lower() == "lock screen":
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

    elif c.lower() == "shutdown system":
            speak("Hold On a Sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')
            
    elif c.lower() == "clear recycle bin":
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

    elif c.lower() == "open notepad":
        speak("opening notepad...")
        os.startfile('notepad.exe')

    elif c.lower().startswith("Set a alarm") or c.lower().startswith("set alarm"):
        try:
            alarm_time = c.lower().split("set alarm at ")[1].strip()
            alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M").time()
            speak(f"Setting alarm at {alarm_time}")
            while datetime.datetime.now().time() < alarm_time:
                time.sleep(1)
            speak("Alarm! Time's up!")
        except ValueError:
            speak("Sorry, I couldn't understand the alarm time. Please try again.")
        except Exception as e:
            speak("Sorry, there was an error setting the alarm.")
            print(f"Error: {e}")

    
    elif c.lower() == "open chrome":
        speak("opening chrome plz a minute sir")
        codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codepath)
    
 
    elif c.lower() == "restart pc":
        subprocess.call(["shutdown", "/r"])

    elif c.lower() == "sleep system":
        speak("Hibernating")
        subprocess.call("shutdown /i /h")

    elif c.lower() == "open calculator":
        speak("opening calculator...")
        os.startfile('calc.exe')


    elif c.lower() == "open word":
        speak("opening word...")
        os.startfile('winword.exe')

    elif c.lower() == "open powerpoint":
        speak("opening powerpoint...")
        os.startfile('powerpnt.exe')

    elif c.lower() == "open email":
        speak("opening email...")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif c.lower() == "tell me about my pc configuration" :
        speak("Here is your PC configuration...")
        cpu_info = cpuinfo.get_cpu_info()
        speak(f"CPU: {cpu_info['brand']} {cpu_info['arch']}")
        speak(f"RAM: {psutil.virtual_memory().total / (1024 * 1024)} MB")
        speak(f"Operating System: {platform.system()} {platform.release()}")
        speak(f"Python Version: {platform.python_version()}")
        
    elif c.lower() == "open camera":
        speak("opening camera...")
        capture_and_show_image()
    
    elif "on spotify" in c.lower():
        song = c.lower().replace("play", "").replace("on spotify", "").strip()
        speak(f"playing {song}...")
        try:
            webbrowser.open(f'https://open.spotify.com/search/{song}')
            pyautogui.leftClick(982,578)
        except:
            speak("Please include 'on spotify' in the command.")

    elif c.lower().startswith("tell me the weather of "):
        city = c.lower().split("tell me the weather of ")[1].strip()
        get_weather(city)

    elif c.lower().endswith('google'):
        search_term = c.lower().split('google', 1)[0].strip()
        if search_term:
            url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
            webbrowser.open(url)
        else :
            speak("Sorry, I couldn't understand your search query. Please try again.")


    elif c.lower().startswith("send whatsapp message to"):
        r = sr.Recognizer()
        phone = c.lower().split("send whatsapp message to ")[1].strip()
        speak(f"sending whatsapp message to {phone}")
        to = phoneNumber.phoneno.get(phone)
        if to:
            speak("What should I say?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                content = r.recognize_google(audio)
            speak(f"message sending to {to}")
            pywhatkit.sendwhatmsg_instantly(to, content)
            pyautogui.click(1839,945)
            speak("message has been sent!")
        else:
            speak(f"Sorry, I don't have an phone number for {phone}.") 
    else:
        aiResponse = aiProcess(c)
        print(f'Ai response: {aiResponse}')
        speak(aiResponse)


def sendEmail(to,content) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('yourmailid@gmail.com', 'your_password')
    server.sendmail('yourmailid@gmail.com', to, f'{content}')
    server.quit()

def capture_and_show_image():

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        speak("Sorry, I couldn't access the camera.")
        return
    
    ret, frame = cap.read()
    if ret:
        speak("Image captured successfully.")
        cv2.imshow('Captured Image', frame)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
        cap.release()
    else:
        speak("Sorry, the image couldn't be captured.")

def greeting():
    current_time = datetime.datetime.now().time()

    morning = datetime.time(6, 0, 0)
    afternoon = datetime.time(12, 0, 0)
    evening = datetime.time(18, 0, 0)
    night = datetime.time(21, 0, 0)

    if morning <= current_time < afternoon:
        return "Good morning! sir,current time is " + str(current_time)
    elif afternoon <= current_time < evening:
        return "Good afternoon! sir"
    elif evening <= current_time < night :
        return "Good morning! sir,current time is " + str(current_time)
    else :
        return "Good morning! sir,current time is " + str(current_time)
    
    

def myname():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Tell me your name")
        print("Tell me your name")
        
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            name = text
            return name
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Please try again.")
            print("Sorry, I couldn't understand. Please try again.")
            return "Unknown"
        except sr.RequestError as e:
            speak("Could not request results from Google Speech Recognition service.")
            print(f"Error: {e}")
            return "Error"


if __name__ == "__main__":
    name = myname()
    speak(f"{name}I am your assistant, tell me {name} how may i help you.")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            print("Speak Now...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said:", text)
                processCommand(text)
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print(f"Sorry, there was an error with the request; {e}")
