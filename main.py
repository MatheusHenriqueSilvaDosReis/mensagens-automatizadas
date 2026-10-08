from datetime import datetime
import pywhatkit as kit
import pyautogui
import time

data_atual = datetime.now()

kit.sendwhatmsg_instantly(
    "+5519992826831",
    "teste de automatização favor nao responda",
    wait_time=30
)