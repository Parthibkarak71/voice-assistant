import pywhatkit
import pyautogui
import speech_recognition as sr

# # Replace with the recipient's phone number (in international format)
# phone_number = "+917908681475" 

# # Your message
# message = "this message is from voice ai"

# # Send the message immediately
# pywhatkit.sendwhatmsg_instantly(phone_number, message)
# import time
# time.sleep(2)
# pyautogui.click(1839,945)
import phoneNumber
name = input("Enter your phone number")
phone = name.strip()
to = phoneNumber.phoneno.get(phone)

message = input("Enter your message")

pywhatkit.sendwhatmsg_instantly(to, message)
pyautogui.click(1839,945)

