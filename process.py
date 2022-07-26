import pyautogui  
import pyperclip
import time

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (link)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# site ta carregando
time.sleep(5) 

# Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta Exportar)
pyautogui.click(x=1073, y=725, clicks=2)

# Passo 3: Download da base de dados

# Passo 4: Calcular