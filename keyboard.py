import pyautogui
pyautogui.FAILSAFE = False  # The failsafe only concerns mouse activity, so set to False

def prev_song():
    pyautogui.press('prevtrack')

if __name__ == '__main__':
    prev_song()
