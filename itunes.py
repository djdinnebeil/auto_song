import win32com.client
import logging
import functools
import os
import subprocess

# Create separate loggers
file_logger = logging.getLogger('FileLogger')
console_logger = logging.getLogger('ConsoleLogger')

# Set logging levels
file_logger.setLevel(logging.INFO)  # Logs detailed info
console_logger.setLevel(logging.INFO)  # Only warnings & errors

# Create file handler for logging to file
file_handler = logging.FileHandler('autosong.log', mode='a')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)

# Create console handler for logging to console
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_formatter)
console_logger.addHandler(console_handler)

# Decorator to log function calls (only to file)
def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        file_logger.info(f'Function called: {func.__name__}')
        result = func(*args, **kwargs)
        file_logger.info(f'Function {func.__name__} completed')
        return result
    return wrapper

def get_itunes_instance():
    """Attempt to get an instance of iTunes."""
    try:
        file_logger.info('Attempting to get iTunes instance.')
        return win32com.client.Dispatch('iTunes.Application')
    except Exception as e:
        file_logger.error(f'Could not connect to iTunes: {e}', exc_info=True)
        console_logger.warning('iTunes is not available. Check if it is running.')
        return None

@log_function_call
def get_current_itunes_song():
    """Retrieve the currently playing song."""
    itunes = get_itunes_instance()
    if not itunes:
        console_logger.warning('iTunes is not running.')
        return 'iTunes is not running.'
    try:
        current_track = itunes.CurrentTrack
        if current_track:
            song_info = f'[{current_track.Name}] [{current_track.Artist}] [{current_track.Album}] [{current_track.Duration}]'
            file_logger.info(f'Currently playing: {song_info}')
            print(song_info)
        else:
            file_logger.info('No song is currently playing.')
            print('No song is currently playing.')
    except Exception as e:
        file_logger.error(f'Error retrieving track info: {e}', exc_info=True)
        print(f'Error retrieving track info: {e}')

@log_function_call
def play_pause_song():
    """Toggle play/pause for the current song."""
    itunes = get_itunes_instance()
    if not itunes:
        return
    try:
        itunes.PlayPause()
        console_logger.info('Play/Pause toggled.')
        file_logger.info('Toggled play/pause.')
    except Exception as e:
        file_logger.error(f'Error toggling play/pause: {e}', exc_info=True)
        console_logger.error('Failed to toggle play/pause.')

@log_function_call
def next_song():
    """Skip to the next track."""
    itunes = get_itunes_instance()
    if not itunes:
        return
    try:
        itunes.NextTrack()
        console_logger.info('Skipped to next song.')
        file_logger.info('Skipped to next song.')
    except Exception as e:
        file_logger.error(f'Error skipping to next song: {e}', exc_info=True)
        console_logger.error('Failed to skip song.')

@log_function_call
def prev_song():
    """Skip to the previous track."""
    itunes = get_itunes_instance()
    if not itunes:
        return
    try:
        itunes.PreviousTrack()
        console_logger.info('Playing previous song.')
        file_logger.info('Playing previous song.')
    except Exception as e:
        file_logger.error(f'Error skipping to previous song: {e}', exc_info=True)
        console_logger.error('Failed to go to previous song.')

@log_function_call
def open_itunes():
    try:
        os.startfile(r"C:\DJ\Software\iTunes\iTunes.exe")
    except Exception as e:
        print("Error opening iTunes:", e)


@log_function_call
def open_itunes_cross_platform():
    itunes_path = r"C:\DJ\Software\iTunes\iTunes.exe"
    try:
        subprocess.Popen(itunes_path)
        print("iTunes opened successfully.")
    except FileNotFoundError:
        print("Error: iTunes executable not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

@log_function_call
def close_itunes_os_taskkill():
    os.system("taskkill /IM iTunes.exe /F")


if __name__ == '__main__':
    close_itunes_os_taskkill()