import pyautogui
pyautogui.FAILSAFE = False  # The failsafe only concerns mouse activity, so set to False

def save_document():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('s')
    pyautogui.keyUp('ctrlleft')

def play_pause_song():
    pyautogui.press('playpause')

def prev_song():
    pyautogui.press('prevtrack')

def next_song():
    pyautogui.press('nexttrack')

if __name__ == '__main__':
    play_pause_song()
