# Voice Assistant

This project is a Python-based voice assistant that can perform various tasks such as opening websites, playing songs, sending emails, retrieving weather information, fetching news, telling jokes, interacting with OpenAI, and controlling system functions like locking the screen or shutting down the PC.

## Features
- Speech Recognition: Uses `speech_recognition` to listen for user commands.
- Text-to-Speech: Uses `pyttsx3` to speak responses.
- OpenAI API Integration: Supports AI-powered responses using the OpenAI API.
- Weather Updates: Retrieves and speaks weather information using the OpenWeatherMap API.
- Jokes: Tells random jokes from the jokes dataset.
- News Headlines: Fetches and reads top news headlines using the NewsAPI.
- Email Sending: Allows the assistant to send emails using the `smtplib`.
- WhatsApp Messaging: Sends WhatsApp messages using `pywhatkit`.
- System Commands: Performs system actions like opening programs, locking the screen, or shutting down.
- PC Configuration: Speaks details about the system's CPU, RAM, and OS.
- Camera Access: Opens the system's camera for capturing live video.

## Requirements
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `requests`
- `gTTS`
- `smtplib`
- `ctypes`
- `winshell`
- `cpuinfo`
- `psutil`
- `cv2`
- `pyautogui`
- `platform`

Setup Instructions
1. Install the required dependencies:
   ```bash
   pip install speechrecognition pyttsx3 pywhatkit requests gtts psutil opencv-python pyautogui

Obtain API keys for:

OpenWeatherMap: for weather updates.
NewsAPI: for fetching news headlines.
OpenAI: for AI-generated responses.

newsapi = "your news api key"
MyApi = "your api key openai"
api_key1 = "your openweathermap api key"

Run the script:
python voiceBot.py

Usage:

Once the script is running, speak commands like:

"Open Google"
"Tell me a joke"
"Play [song name]"
"Send email to [contact]"
"Tell me a news"
"What's the weather in [city]"
"Lock screen"
"What is the time"


Customization:

Add more commands: Extend the processCommand function to handle additional tasks.
Modify responses: Update the speak function for personalized responses.


This `README.md` covers the essential aspects of setting up and using the voice assistant.



