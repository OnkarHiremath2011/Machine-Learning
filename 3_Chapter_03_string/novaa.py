"""
Orvision Personal Assistant (single-file)
- Wake word: "hello orvision"
- Speech recognition with SpeechRecognition (Google API by default)
- TTS with pyttsx3 (male voice preference)
- Automation with webbrowser, subprocess, os, pyautogui
- NOTE: Configure safe email sending if you want "send email" feature.

Install required packages:
pip install SpeechRecognition pyttsx3 pywhatkit pyautogui keyboard pyperclip playsound pyaudio
"""

import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
import sys
import threading
import time
import pyautogui
import pyperclip
import platform
import smtplib
from email.message import EmailMessage
import getpass

# ------------- Configuration -------------
WAKE_WORD = "hello orvision"
TYPING_DELAY = 0.02
CHATGPT_INPUT_TAB_COUNT = 8
ALLOW_DESTRUCTIVE = False
DESTRUCTIVE_PASSWORD = "orvision-safe-pass"
# -----------------------------------------

# Setup TTS (male voice preferred)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
male_voice_id = None
for v in voices:
    name = (v.name + " " + (v.id or "")).lower()
    if "male" in name or "david" in name or "peter" in name or "english" in name:
        male_voice_id = v.id
        break
if male_voice_id is None and len(voices) > 0:
    male_voice_id = voices[0].id
if male_voice_id:
    engine.setProperty('voice', male_voice_id)
engine.setProperty('rate', 160)

import pyttsx3
import threading

engine = pyttsx3.init()

def speak(text):
    def run_speech():
        local_engine = pyttsx3.init()  # fresh engine avoids conflicts
        local_engine.say(text)
        local_engine.runAndWait()
        local_engine.stop()

    threading.Thread(target=run_speech).start()

recognizer = sr.Recognizer()
mic = None
try:
    mic = sr.Microphone()
except Exception:
    print("Warning: Microphone not available. Voice features will not work.")
    mic = None

def listen(timeout=6, phrase_time_limit=8):
    if mic is None:
        return None
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except:
            return None

def open_website(url):
    webbrowser.open_new_tab(url)
    speak(f"Opening {url}")

def web_search(query):
    url = "https://www.google.com/search?q=" + webbrowser.quote(query)
    open_website(url)

def open_chatgpt_and_search(query):
    chat_url = "https://chat.openai.com/"
    open_website(chat_url)
    time.sleep(3)
    web_search(query)
    try:
        speak("Attempting to paste your question into ChatGPT.")
        time.sleep(4)
        pyperclip.copy(query)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    except Exception as ex:
        print("Could not auto-type into ChatGPT:", ex)
        speak("Couldn't type into ChatGPT, but I opened it and searched the web.")

def open_app(app_name):
    plat = platform.system().lower()
    app_name_lower = app_name.lower()
    speak(f"Trying to open {app_name}")
    try:
        if "chrome" in app_name_lower:
            webbrowser.open_new_tab("https://www.google.com")
            return
        if plat == "windows":
            mapping = {
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "cmd": "cmd.exe",
                "powershell": "powershell.exe"
            }
            for key, path in mapping.items():
                if key in app_name_lower:
                    subprocess.Popen(path, shell=True)
                    return
            subprocess.Popen(f'start "" "{app_name}"', shell=True)
        elif plat == "linux":
            subprocess.Popen([app_name])
        elif plat == "darwin":
            subprocess.Popen(["open", "-a", app_name])
    except Exception:
        speak("Failed to open the app.")

def play_youtube(query):
    import pywhatkit
    speak(f"Playing {query} on YouTube")
    try:
        pywhatkit.playonyt(query)
    except:
        speak("Couldn't play YouTube automatically.")

def send_email_smtp(to_email, subject, body, smtp_config=None):
    if smtp_config is None:
        speak("Email sending requires SMTP settings.")
        return False
    try:
        msg = EmailMessage()
        msg['From'] = smtp_config['username']
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.set_content(body)
        server = smtplib.SMTP(smtp_config['host'], smtp_config['port'], timeout=20)
        if smtp_config.get('use_tls', True):
            server.starttls()
        server.login(smtp_config['username'], smtp_config['password'])
        server.send_message(msg)
        server.quit()
        speak("Email sent.")
        return True
    except Exception:
        speak("Failed to send email.")
        return False

def take_screenshot(save_path=None):
    if save_path is None:
        save_path = os.path.join(os.getcwd(), f"orvision_screenshot_{int(time.time())}.png")
    image = pyautogui.screenshot()
    image.save(save_path)
    speak(f"Screenshot saved to {save_path}")
    return save_path

def open_file(path):
    if not os.path.exists(path):
        speak("File not found: " + path)
        return
    try:
        if platform.system().lower() == "windows":
            os.startfile(path)
        elif platform.system().lower() == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
        speak("Opened file.")
    except:
        speak("Couldn't open the file.")

def handle_command(command):
    if not command:
        return
    print("Heard command:", command)
    if "open chatgpt" in command:
        if "search" in command:
            query = command.split("search",1)[1].strip()
            if not query:
                speak("What should I search in ChatGPT?")
                return
            open_chatgpt_and_search(query)
        else:
            open_website("https://chat.openai.com/")
            speak("Opened ChatGPT.")
        return

    if command.startswith("search ") or command.startswith("google "):
        query = command.split(" ",1)[1]
        web_search(query)
        return

    if command.startswith("open "):
        target = command.replace("open ","",1).strip()
        open_app(target)
        return

    if "play youtube" in command or command.startswith("play "):
        if "youtube" in command:
            query = command.split("play",1)[1].replace("on youtube","").strip()
        else:
            query = command.split("play",1)[1].strip()
        if query:
            play_youtube(query)
        else:
            speak("What should I play on YouTube?")
        return

    if "take screenshot" in command:
        path = take_screenshot()
        return

    if command.startswith("open file"):
        parts = command.split(" ",2)
        if len(parts) >= 3:
            open_file(parts[2])
        else:
            speak("Please give the full path.")
        return

    if "who are you" in command or "what is your name" in command:
        speak("I am Orvision, your personal assistant.")
        return

    speak(f"Searching the web for: {command}")
    web_search(command)

def continuous_listen_loop():
    speak("Orvision is online. Say 'hello orvision' to wake me.")
    while True:
        text = listen(timeout=8, phrase_time_limit=6)
        if text and WAKE_WORD in text:
            speak("Yes? How can I help?")
            cmd = listen(timeout=6, phrase_time_limit=12)
            if cmd:
                cmd = cmd.replace(WAKE_WORD, "").strip()
                handle_command(cmd)
            else:
                typed = input("Type a command: ")
                if typed.strip():
                    handle_command(typed.strip().lower())
        time.sleep(0.3)

def start_orvision():
    listen_thread = threading.Thread(target=continuous_listen_loop, daemon=True)
    listen_thread.start()
    speak("You can also type commands here. Type 'exit' to quit.")
    while True:
        try:
            cmd = input("Orvision> ").strip().lower()
            if cmd in ["exit","quit"]:
                speak("Goodbye.")
                sys.exit(0)
            if cmd:
                handle_command(cmd)
        except KeyboardInterrupt:
            speak("Exiting. Bye.")
            sys.exit(0)

if __name__ == "__main__":
    start_orvision()
