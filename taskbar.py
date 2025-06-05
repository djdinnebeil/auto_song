import pyautogui

def send_winkey(position):
    """Sends 'Win + n' (0–9) on Windows using pyautogui."""
    position = f'{position}'
    pyautogui.keyDown('winright')
    pyautogui.press(position)
    pyautogui.keyUp('winright')

send_winkey(0)
