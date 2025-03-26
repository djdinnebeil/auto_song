import pyperclip

def copy_to_clipboard(text: str):
    """Copy the given text to the system clipboard."""
    pyperclip.copy(text)

if __name__ == '__main__':
    copy_to_clipboard('hey ya')
