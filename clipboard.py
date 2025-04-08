import pyperclip
import pyautogui
from time import sleep

pyautogui.FAILSAFE = False  # The failsafe only concerns mouse activity, so set to False

def copy_to_clipboard(text: str):
    """Copy the given text to the system clipboard."""
    pyperclip.copy(text)

def paste_from_clipboard():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('v')
    pyautogui.keyUp('ctrlleft')


if __name__ == '__main__':
    copy_to_clipboard('hey ya')
    sleep(1)
    paste_from_clipboard()
