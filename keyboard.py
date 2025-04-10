import pyautogui
pyautogui.FAILSAFE = False  # The failsafe only concerns mouse activity, so set to False

def prev_song():
    pyautogui.press('prevtrack')

def next_song():
    pyautogui.press('nexttrack')

if __name__ == '__main__':
    next_song()
