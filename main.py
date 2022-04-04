# pip install -r requirements.txt
import datetime
from multiprocessing import Process
import os
import pickle
import random
import re
import smtplib
import threading
import wave
import webbrowser
from urllib.request import urlopen
import nltk
import numpy as np
import pyaudio
import pyjokes
import pywhatkit as kt
import requests
import speech_recognition as sr
import wikipedia
import geocoder
from win10toast import ToastNotifier
from PyDictionary import PyDictionary
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtWidgets import QMainWindow, QApplication, QSizeGrip, QSlider, QLabel
from bs4 import BeautifulSoup as soup
from googletrans import Translator
from gtts import gTTS
from mutagen.mp3 import MP3
from nltk.stem import WordNetLemmatizer
from playsound import playsound
from pydub import AudioSegment
from pynput import keyboard
from tensorflow.keras.models import load_model

import json
# Main Window GUI File
from interface import *
# Splash Screen GUI File
from splashScreen import *
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

dictionary = PyDictionary()
translator = Translator()

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('chatbot/intents.json').read())
words = pickle.load(open('chatbot/words.pkl', 'rb'))
classes = pickle.load(open('chatbot/classes.pkl', 'rb'))
model = load_model('chatbot/chatbotmodel.h5')

response = None
lang = 'en'
lang_code = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}

counter = 0


############################################################################################################
####                                   Application : Splash_Screen                                      ####
############################################################################################################

# Splash-Screen Window
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # Remove Window Titlebar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # QTimer ==> Start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in MiliSeconds
        self.timer.start(20)

        # Change Discription

        # Intial Discription
        self.ui.Discription.setText("<strong>Welcome</strong> to ALITA")

        # Change Textb
        QtCore.QTimer.singleShot(2300, lambda: self.ui.Discription.setText(
            "Your Personal <strong>Virtual Assistant</strong>"))
        QtCore.QTimer.singleShot(3700,
                                 lambda: self.ui.Discription.setText("Loading <strong>Your Application </strong>"))

        self.show()

    def progress(self):
        global counter

        # set Value to progress bar
        self.ui.progressBar.setValue(counter)

        # close splashScreen and open main window
        if counter > 100:
            # stop timer
            self.timer.stop()

            # show main window
            self.main = MainWindow()
            self.main.show()

            # close splashScreen
            self.close()

        # increase counter
        counter += 1


############################################################################################################
####                                   Application : Main Window                                        ####
############################################################################################################


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ################################################################################################
        ####                                  QSlider - Volume Adjust                               ####
        ################################################################################################

        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.slider.valueChanged.connect(self.changed_Slider)

        self.label = self.findChild(QLabel, "VolumeValue")

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)

        print(self.ui.VolumeValue.text())

        #################################################################################################
        ####                                       PAGES Connectors                                  ####
        #################################################################################################

        # set the page that will appear default when Application is Opened #
        json_data = open('json/userInfo.json', 'r')
        obj = json.load(json_data)
        for i in range(len(obj)):
            name = obj[i].get("Name")
            email = obj[i].get("Email")
            dob = obj[i].get("DOB")
        if not obj:
            self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.greetPage)
            self.ui.label_16.setText(name)
            self.ui.label_17.setText(email)
            self.ui.label_18.setText(dob)

        # Back to Greet Page #
        self.ui.backBtn.clicked.connect(lambda: self.backBtnInfoCheck())

        # Back to Main Page #
        self.ui.LogOut.clicked.connect(lambda: self.userLogout())

        #  Log Out #
        self.ui.proceedBtn.clicked.connect(lambda: self.userInfo())

        # Profile Page #
        self.ui.profileBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profilePage))

        # Settings Page #
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settingsPage))

        # Feedback Page #
        self.ui.feedbackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.feedbackPage))

        # App Version Page #
        self.ui.appVersionBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.appVersionPage))

        # About Alita Page #
        self.ui.aboutBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.aboutPage))

        #######################################################################################################

        # Remove Window Titlebar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # window Size grip to resize window
        QSizeGrip(self.ui.size_grip)

        ################################################################################################
        ####                              Button Click connectors                                   ####
        ################################################################################################

        # Minimize Window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        # Close Window
        self.ui.close_window_button.clicked.connect(lambda: self.close())

        # Exit Window
        self.ui.exit_button.clicked.connect(lambda: self.close())

        # Restore/Maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        # left menu toggle button
        self.ui.open_close_sidebar_button.clicked.connect(lambda: self.slideLeftMenu())

        # When you click mic button or press Enter, it will send the text to the label throgh the clicker() function
        self.ui.sendTextField.returnPressed.connect(lambda: self.clicker())

        # when you click button it will clear the text fields.
        self.ui.sendFdbk.clicked.connect(lambda: self.sendFeedbackBtn())

        # Change button icons when user starts typing in text field
        self.ui.sendTextField.textChanged.connect(lambda: self.changeIcontoSend())
        self.ui.sendTextField.editingFinished.connect(lambda: self.changeIcontomic())

        # CSS for chat bubble
        self.ui.chat.setStyleSheet("padding:20px;"
                                   "color: white;")

        ##########################################################################################################

        self.ui.MicBtn.clicked.connect(lambda: self.recordQuery())

        # Ending of all the Statements and connectors

        self.show()  # It will load and show you the main Window application
        # p1 = multiprocessing.Process(target=alitaFunction(), args=())
        # p1.start()
        # p1.join()

    def backBtnInfoCheck(self):
        if self.ui.Name.text() == "" or self.ui.Email.text() == "":
            self.ui.Name.setPlaceholderText("Name is required")
            self.ui.Email.setPlaceholderText("Email is required")
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.greetPage)

    def userLogout(self):
        new_data = []
        with open("json/userInfo.json", "r") as f:
            temp = json.load(f)
            delete_item = 0
            i = 0
            for y in temp:
                if i == int(delete_item):
                    pass
                    i += 1
                else:
                    new_data.append(y)
                    i += 1
            with open("json/userInfo.json", "w") as x:
                json.dump(new_data, x, indent=4)
            self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage)

    def userInfo(self):
        name = self.ui.Name.text()
        email = self.ui.Email.text()
        dob = self.ui.dateEdit.date().toPyDate()

        if name == "" or email == "":
            self.ui.Name.setPlaceholderText("Name is required")
            self.ui.Email.setPlaceholderText("Email is required")

        else:
            def add(data, path="json/userInfo.json"):
                with open(path, "w") as f:
                    json.dump(data, f, indent=4)

            with open("json/userInfo.json") as json_file:
                obj = json.load(json_file)
                item = {
                    "Name": str(name),
                    "Email": str(email),
                    "DOB": str(dob)
                }
                obj.append(item)
            add(obj)

            self.ui.stackedWidget.setCurrentWidget(self.ui.greetPage)
            self.ui.label_16.setText(name)
            self.ui.label_17.setText(email)
            self.ui.label_18.setText(str(dob))

    # Functions to Change button icons when user starts typing in text field
    def changeIcontoSend(self):
        self.ui.MicBtn.setIcon(QtGui.QIcon(u":/iconLogos/icons/send.svg"))

    def changeIcontomic(self):
        self.ui.MicBtn.setIcon(QtGui.QIcon(u":/iconLogos/icons/mic.svg"))

    # Function to clear the text fields after submitting or clicking the submit btn
    def sendFeedbackBtn(self):
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('the.alita1@gmail.com', 'theElite1isFinish')
        mail.sendmail('the.alita1@gmail.com', 'the.alita1@gmail.com', str(self.ui.enterFdbk.toPlainText()))
        mail.close()
        self.speak("Thank you for your feedback.Its been sent")
        self.ui.nameFdbk.setText(self.ui.label_16.text())
        self.ui.emailFdbk.setText(self.ui.label_17.text())
        self.ui.stackedWidget.setCurrentWidget(self.ui.greetPage)

    # Function to send written text to the label
    def clicker(self):
        msg = self.ui.sendTextField.text()
        self.addTextToChat(msg, True)
        self.ui.sendTextField.clear()
        self.taskExecution(msg)

    def addTextToChat(self, msg, user):
        chat = self.ui.chat.text()
        if user:
            chat = chat + '<div style="text-align:right;">' + msg + '</div>'
        else:
            chat = chat + '<div>' + msg + '</div>'
        self.ui.chat.setText(str(chat))

    # Slider set Value function
    def changed_Slider(self):
        value = self.slider.value()
        self.label.setText(str(value))

    def restore_or_maximize_window(self):
        # if window is maximized
        if self.isMaximized():
            self.showNormal()
            # change icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/iconLogos/icons/maximize.svg"))
        else:
            self.showMaximized()
            # change icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/iconLogos/icons/minimize-2.svg"))

        ################################################################################################
        ####                                    Move Window                                         ####
        ################################################################################################

    # Function to move window on mouse drag event on title bar
    def moveWindow(self, e):
        # detect if the window is normal size
        if not self.isMaximized():  # not maximized
            # move window only when it is normal size
            # if left mouse button is clicked(Only accepts left button)
            if e.buttons() == Qt.LeftButton:
                # move window
                self.move(self.pos() + e.globalpos() - self.clickPosition)
                self.clickPosition = e.globalpos()
                e.accept()

        # add click event/mouse move event/ drag event to the top header to move the window
        self.ui.Header_frame.mouseMovement = self.moveWindow

    # Add mouse events to the window
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # we will use this value to move the window

        ###############################################################################################
        ####                                    Left Toggle Menu                                   ####
        ###############################################################################################

    # Slide left menu function
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.side_menu_container.width()

        # if Minimized
        if width == 0:
            # Expand menu
            newWidth = 300
            self.ui.open_close_sidebar_button.setIcon(QtGui.QIcon(u":/iconLogos/icons/chevron-left.svg"))
        # if Maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.open_close_sidebar_button.setIcon(QtGui.QIcon(u":/iconLogos/icons/align-justify.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.side_menu_container, b"maximumWidth")  # Animate minimumwidth
        self.animation.setDuration(500)
        self.animation.setStartValue(width)  # start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def alitaFunction(self):
        while True:
            query = self.takeCommand().lower()
            if re.search('alita|aleta|paoletta', query):
                playsound('sounds/wakeupSleepSound.wav')
                self.recordQuery()

    def speak(self, audio):
        if lang != 'en':
            audio = translate(audio, lang, 'en')

        print(audio)
        self.addTextToChat(audio, False)

        tts = gTTS(text=audio, lang=lang, slow=False)
        filename = "sounds/voice.mp3"
        try:
            os.remove(filename)
        except OSError:
            pass
        tts.save(filename)

        sound = AudioSegment.from_mp3("sounds/voice.mp3")
        sound.export("sounds/voice.wav", format="wav")
        audio = MP3("sounds/voice.mp3")

        wf = wave.open("sounds/voice.wav", 'rb')
        p = pyaudio.PyAudio()

        def callback(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            return data, pyaudio.paContinue

        # open stream using callback
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        stream_callback=callback)

        # start the stream
        stream.start_stream()

        user = threading.Thread(target=user_input)
        user.daemon = True
        user.start()
        print("Press space to end.")
        user.join(audio.info.length)
        if response is None:
            print('Exiting because audio ended')
        elif response is True:
            print('stopping on your command')

        # stop stream
        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning! how can i help you ?")

        elif 12 <= hour < 18:
            self.speak("Good Afternoon! how can i help you ?")

        else:
            self.speak("Good Evening! how can i help you ?")

    def takeCommand(self):
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)

            try:
                print("Recognizing...")
                new_query = r.recognize_google(audio, language=lang)
                # MainWindow.addTextToChat(f"User said: {new_query}\n", True)
                print(f"User said: {new_query}\n")
                if lang != 'en':
                    new_query = translate(new_query, 'en', lang)
                return new_query

            except Exception as e:
                print(e)
                print("Say that again please...")

    def calc(self, query1):
        operations = ['+', '-', '/', '*']
        query2 = query1.split()
        for i in query2:
            if not isNumber(i) and i not in operations:
                print(i)
                self.speak("Sorry, seems like there is an issue calculating. Please try again.")
                return
        result = eval(query1)
        self.speak("Its " + str(result))

    def getWeather(self):
        g = geocoder.ip('me')

        api_key = "84d49b3dbcd80c5cd137642159620727"
        base_url = "http://api.openweathermap.org/data/2.5/weather?q="

        final_url = base_url + g.city + "&units=metric&appid=" + api_key

        # this variable contain the JSON data which the API returns
        response = requests.get(final_url)

        weather_data = response.json() if response and response.status_code == 200 else None
        if weather_data:
            c_temp = weather_data['main']['temp']
            self.speak("The current weather in your area is " + str(round(c_temp)) + "° Celsius.")
        else:
            webbrowser.open("weather.com")
            self.speak("I am not able to retrieve data for you! opened weather.com for you!")

    def toDoList(self, query):
        if re.search("add", query):
            self.speak("what would you like to add into the to-do list ?")
            listItem = self.takeCommand()

            def add(data, path="json/todo.json"):
                with open(path, "w") as f:
                    json.dump(data, f, indent=4)

            with open("json/todo.json") as json_file:
                obj = json.load(json_file)
                x = {"item": str(listItem)}
                obj.append(x)
            add(obj)
            self.speak(f"i have added {listItem} to your list")
        elif re.search("delete", query):
            self.speak("what would you like to delete from the to-do list ?")
            listItem = self.takeCommand()
            new_data = []
            with open("json/todo.json", "r") as f:
                temp = json.load(f)
                for x in range(len(temp)):
                    if listItem == (temp[x].get("item")):
                        con = x

                delete_item = con
                i = 0
                for y in temp:
                    if i == int(delete_item):
                        pass
                        i += 1
                    else:
                        new_data.append(y)
                        i += 1
                with open("json/todo.json", "w") as x:
                    json.dump(new_data, x, indent=4)
            self.speak(f"I have deleted the {listItem} from your list")
        else:
            json_data = open('json/todo.json', 'r')
            obj = json.load(json_data)
            if len(obj) == 0:
                self.speak("Your to-do list is empty at the moment.")
            else:
                self.speak("Your to-do list contains :")
                for i in range(len(obj)):
                    self.speak(obj[i].get("item"))

    def myDictionary(self, query):
        if re.search("meaning|mean", query):
            if "of" in query:
                index = query.index("of")
                index = index + 2
                query = query[index:]
            elif "my" in query:
                index = query.index("of")
                index = index + 2
                query = query[index:]
            else:
                index = query.index("by")
                index = index + 2
                query = query[index:]

            word = dictionary.meaning(query)
            i = 0
            if i <= 0:
                for state in word:
                    print(word[state])
                    self.speak(f"{query} means ".format(query) + str((word[state])[:1]))
                    i += 1

        elif re.search("synonym", query):
            index = query.index("of")
            index = index + 2
            query = query[index:]

            word = dictionary.synonym(str(query), 'en')
            print(word)

        elif re.search("antonym", query):
            index = query.index("of")
            index = index + 2
            query = query[index:]

            word = dictionary.antonym(query)
            i = 0
            if i <= 0:
                for state in word:
                    print(word[state])
                    self.speak(f"{query} means ".format(query) + str((word[state])[:1]))
                    i += 1

    def translatedSpeech(self, audio, dest_lang):
        print(audio)
        self.addTextToChat(audio, False)
        tts = gTTS(text=audio, lang=dest_lang, slow=False)
        filename = "sounds/voice.mp3"
        try:
            os.remove(filename)
        except OSError:
            pass
        tts.save(filename)
        playsound(filename)

    def myTranslator(self, query):
        global lang_code
        dest_lang = 'en'
        print(query)
        for code in lang_code:
            if re.search(lang_code[code], query):
                dest_lang = code
                break

        self.speak("what would you like to translate into " + lang_code[dest_lang] + "?")
        transcript = self.takeCommand()
        result = translate(transcript, dest_lang, lang)
        self.speak("in " + lang_code[dest_lang] + " that's ")
        self.translatedSpeech(result, dest_lang)

    def getNews(self):
        news_url = "https://news.google.com/news/rss"
        client = urlopen(news_url)
        xml_page = client.read()
        client.close()
        soup_page = soup(xml_page, "lxml")
        news_list = soup_page.findAll("item")
        li = []
        for news in news_list[:2]:
            temp = news.title.text.encode('utf-8')
            index = str(temp).find(" - ")
            news = str(temp[:(index - 2)])
            news = news[1:]
            print(news)
            li.append(str(news))
        webbrowser.open('news.google.com/news')
        self.speak("The latest breaking news updates are: " + li[0] + " and " + li[1])

    def sendFeedback(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.feedbackPage)
        self.ui.nameFdbk.setText(self.ui.label_16.text())
        self.ui.emailFdbk.setText(self.ui.label_17.text())
        self.speak(f"Sure, here you go {self.ui.label_16.text()}.")

    def website_opener(self, domain):
        extension = re.search(r"[.]", domain)
        if not extension:
            if not domain.endswith(".com"):
                domain = domain + ".com"
        try:
            url = 'https://www.' + domain
            webbrowser.open(url)
            self.speak("Opening " + domain)
            return True
        except Exception as e:
            print(e)
            return False

    def open_app(self, name):
        print(name)
        app_codes = {
            "chrome": "start chrome",
            "edge": "start msedge",
            "notepad": "start notepad",
            "excel": "start excel",
            "explorer": "start explorer",
            "files": "start explorer",
            "word": "start winword",
            "powerpoint": "start powerpnt",
            "calculator": "start calc",
            "task manager": "start taskmgr",
            "paint": "start mspaint",
            "music": "start wmplayer",
            "code": "code"
        }
        cmd = app_codes.get(name)
        if cmd is None:
            self.website_opener(name)
        else:
            self.speak("launching " + name)
            os.system(app_codes[name])

    def recordQuery(self):
        query = self.takeCommand().lower()
        self.addTextToChat(query, True)
        self.taskExecution(query)

    def taskExecution(self, query):
        global lang
        # Logic for executing tasks based on query

        if re.search("f\*\*\*|b\*\*\*\*|a\*\*\*\*\*\*|motherfuker", query):
            ints = predict_class(query)
            res = get_response(ints, intents)
            self.speak(res)

        elif re.search('what can you do|tasks can you perform|what things you can help me with|life easy|what features',
                       query):
            ints = predict_class(query)
            res = get_response(ints, intents)
            self.speak(res)

        elif re.search('change language', query):
            query = query.replace("change language to", "")
            for code in lang_code:
                if re.search(lang_code[code], query):
                    lang = code
                    self.speak("language changed to " + query)
                    break

        elif re.search('reminder|remind', query):
            self.speak("What would you like me to remind you?")
            remindData = self.takeCommand()
            self.speak("when should i remind you?")
            timeQuery = self.takeCommand().lower()

            if "seconds" in timeQuery:
                timeQuery = timeQuery.isdigit
                duration = int(timeQuery)
                self.speak("Reminder is set for you")
                p1 = Process(target=reminder, args=(remindData, duration,))
                p1.start()

            elif "minutes" in timeQuery:
                timeQuery = timeQuery.isdigit
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60
                duration = timeQuery
                self.speak("Reminder is set for you")
                p1 = Process(target=reminder, args=(remindData, duration,))
                p1.start()

            elif "minute" in timeQuery:
                timeQuery = timeQuery.isdigit
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60
                duration = timeQuery
                self.speak("Reminder is set for you")
                p1 = Process(target=reminder, args=(remindData, duration,))
                p1.start()

            elif "hours" in timeQuery:
                timeQuery = timeQuery.isdigit
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60 * 60
                duration = timeQuery
                self.speak("Reminder is set for you")
                p1 = Process(target=reminder, args=(remindData, duration,))
                p1.start()

            elif "hour" in timeQuery:
                timeQuery = timeQuery.isdigit
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60 * 60
                duration = timeQuery
                self.speak("Reminder is set for you")
                p1 = Process(target=reminder, args=(remindData, duration,))
                p1.start()

        elif re.search('timer', query):
            self.speak("For how long?")
            timeQuery = self.takeCommand().lower()

            if "seconds" in timeQuery:
                timeQuery = timeQuery.isdigit()
                duration = int(timeQuery)
                self.speak("Timer is set.")
                p1 = Process(target=timer, args=("Timer is up", duration,))
                p1.start()

            elif "minutes" in timeQuery:
                timeQuery = timeQuery.isdigit()
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60
                duration = timeQuery
                self.speak("timer is set.")
                p1 = Process(target=timer, args=("Timer is up", duration,))
                p1.start()

            elif "minute" in timeQuery:
                timeQuery = timeQuery.isdigit()
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60
                duration = timeQuery
                self.speak("Timer is set.")
                p1 = Process(target=timer, args=("Timer is up", duration,))
                p1.start()

            elif "hours" in timeQuery:
                timeQuery = timeQuery.isdigit()
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60 * 60
                duration = timeQuery
                self.speak("Timer is set")
                p1 = Process(target=timer, args=("Timer is up", duration,))
                p1.start()

            elif "hour" in timeQuery:
                timeQuery = timeQuery.isdigit()
                timeQuery = int(timeQuery)
                timeQuery = timeQuery * 60 * 60
                duration = timeQuery
                self.speak("Timer is set")
                p1 = Process(target=timer, args=("Timer is up", duration,))
                p1.start()

        elif re.search('alarm', query):
            x = 43200
            crntHour = datetime.datetime.now().strftime("%I")
            print(crntHour)
            crntHour = int(crntHour)
            if crntHour == 12:
                crntHour = 0
            crntHour = crntHour * 3600
            print(crntHour)
            crntMin = datetime.datetime.now().strftime("%M")
            crntx = datetime.datetime.now().strftime("%p")
            crntMin = int(crntMin) * 60
            crntTime = crntHour + crntMin
            self.speak("For what time?")
            timeQuery = self.takeCommand().lower()
            if "a.m." in timeQuery:
                a = "AM"
            else:
                a = "PM"
            timeQuery = timeQuery.replace(":", "")
            timeQuery = timeQuery.replace("a.m.", "")
            timeQuery = timeQuery.replace("p.m.", "")
            if crntx == a:
                if len(timeQuery) == 4:
                    setHour = timeQuery[0]
                    setHour = int(setHour) * 3600
                    setMin = timeQuery[1] + timeQuery[2]
                    setMin = int(setMin) * 60
                    setTime = setHour + setMin
                    duration = setTime - crntTime
                    self.speak("Alarm is set")
                    p1 = Process(target=alarm, args=("Alarm is off now", duration))
                    p1.start()
                else:
                    setHour = timeQuery[0] + timeQuery[1]
                    if crntHour == 0:
                        setHour = 0
                    setHour = int(setHour) * 3600
                    setMin = timeQuery[2] + timeQuery[3]
                    setMin = int(setMin) * 60
                    setTime = setHour + setMin
                    duration = setTime - crntTime
                    self.speak("Alarm is set")
                    p1 = Process(target=alarm, args=("Alarm is off now", duration))
                    p1.start()
            else:
                if len(timeQuery) == 4:
                    setHour = timeQuery[0]
                    setHour = int(setHour) * 3600
                    setMin = timeQuery[1] + timeQuery[2]
                    setMin = int(setMin) * 60
                    setTime = setHour + setMin
                    duration = x - crntTime + setTime
                    self.speak("Alarm is set")
                    p1 = Process(target=alarm, args=("Alarm is off now", duration))
                    p1.start()
                else:
                    setHour = timeQuery[0] + timeQuery[1]
                    setHour = int(setHour) * 3600
                    setMin = timeQuery[2] + timeQuery[3]
                    setMin = int(setMin) * 60
                    setTime = setHour + setMin
                    duration = x - crntTime + setTime
                    self.speak("Alarm is set")
                    p1 = Process(target=alarm, args=("Alarm is off now", duration))
                    p1.start()

        elif re.search('wikipedia|who is|tell me about', query):
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=1)
            self.speak(f"According to Wikipedia " + results)

        elif re.search('send an email|send email', query):
            webbrowser.open_new_tab("mailto:")
            self.speak("sure here you go.")

        elif re.search('open youtube and search', query):
            query = query.replace("Alita", "")
            query = query.replace("open youtube and search" or "open youtube and search for", "")
            webResult = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(webResult)
            self.speak("This what I found on youtube.")

        elif re.search('to-do list|to do list', query):
            self.toDoList(query)

        elif re.search('google', query):
            query = query.replace("google", "")
            query = query.replace("search", "")
            query = query.replace("for", "")
            query = query.replace("open", "")
            query = query.replace("and", "")
            kt.search(query)
            self.speak("Here is what I found on google.")

        elif re.search('news', query):
            self.getNews()

        elif re.search("motivation|inspiration|motivate|inspire|influence me", query):
            ints = predict_class(query)
            res = get_response(ints, intents)
            self.speak(res)

        elif re.search('open|launch', query):
            query = query.replace("open ", "")
            query = query.replace("launch ", "")
            self.open_app(str.strip(query))

        elif re.search('play music', query):
            webbrowser.open("https://music.youtube.com/")
            self.speak("Here's what i found.")

        elif re.search('time', query):
            strTime = datetime.datetime.now().strftime("%I %M %p")
            self.speak(f"Its {strTime}")

        elif re.search('date', query):
            strDate = datetime.datetime.now().strftime("%A %B %d %Y")
            self.speak(f"Its {strDate}")

        elif re.search('weather|temperature', query):
            self.getWeather()

        elif re.search('meaning|mean|definition|explanation', query):
            self.myDictionary(query)

        elif re.search('translate|interpret', query):
            if re.search("translate something|translate anything", query):
                self.speak("in which language would you like to translate ?")
                query = self.takeCommand().lower()
                self.myTranslator(query)
            else:
                self.myTranslator(query)

        elif re.search('joke|entertain|laugh|comedy', query):
            self.speak(pyjokes.get_joke(language='en'))

        elif re.search('feedback', query):
            self.sendFeedback()

        elif re.search('fact|educate|impress', query):
            ints = predict_class(query)
            res = get_response(ints, intents)
            self.speak("did you know? " + res)

        elif re.search('sleep', query):
            ints = predict_class(query)
            res = get_response(ints, intents)
            self.speak(res)
            playsound('sounds/wakeupSleepSound.wav')

        elif re.search('thank', query):
            ints = predict_class(query)
            res = get_response(ints, intents)
            self.speak(res)
            playsound('sounds/wakeupSleepSound.wav')

        elif re.search('\+|-|\*|\/|calc', query):
            if re.search("pi",query):
                self.speak("Calculating value of pi.")
                self.speak("pi = 3.141592653589793238")
            else:
                query = query.replace("calculate", "")
                query = query.replace("what is", "")
                query = query.replace("into", "*")
                self.calc(query)

        else:
            ints = predict_class(query)
            res = get_response(ints, intents)
            self.speak(res)

    ########################################################################################################
    ####                                        EXECUTE APP                                             ####
    ########################################################################################################


# Backend(do not touch if you do not understand)
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.1
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def on_press(key):
    if key != keyboard.Key.space:
        return True
    return False


def user_input():
    global response
    with keyboard.Listener(on_press=on_press) as listener:
        response = listener.join()


def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


def translate(transcript, dest_lang, src_lang):
    res = translator.translate(transcript, dest=dest_lang, src=src_lang)
    return res.text


def reminder(remindData, duration):
    notificator = ToastNotifier()
    notificator.show_toast(f"Reminder", remindData, duration=duration)


def timer(timerData, duration):
    notificator = ToastNotifier()
    playsound('sounds/timerSound.wav')
    notificator.show_toast(f"Clock", timerData, duration=duration)


def alarm(alarmData, duration):
    print(duration)
    notificator = ToastNotifier()
    notificator.show_toast(f"Alarm", alarmData, duration=duration)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

    ############################################### END ####################################################
