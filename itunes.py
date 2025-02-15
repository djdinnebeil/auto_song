import win32com.client
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_itunes_instance():
    """Attempt to get an instance of iTunes."""
    try:
        return win32com.client.Dispatch('iTunes.Application')
    except Exception as e:
        logging.error(f'Could not connect to iTunes: {e}')
        return None

def get_current_itunes_song():
    """Retrieve the currently playing song."""
    itunes = get_itunes_instance()
    if not itunes:
        return 'iTunes is not running.'

    try:
        current_track = itunes.CurrentTrack
        if current_track and current_track.Name and current_track.Artist:
            return f'{current_track.Name} - {current_track.Artist}'
        else:
            return 'No song is currently playing.'
    except Exception as e:
        return f'Error retrieving track info: {e}'

def play_pause_song():
    """Toggle play/pause for the current song."""
    itunes = get_itunes_instance()
    if not itunes:
        return

    try:
        itunes.PlayPause()
        logging.info('Toggled play/pause.')
    except Exception as e:
        logging.error(f'Error toggling play/pause: {e}')

def next_song():
    """Skip to the next track."""
    itunes = get_itunes_instance()
    if not itunes:
        return

    try:
        itunes.NextTrack()
        logging.info('Skipped to next song.')
    except Exception as e:
        logging.error(f'Error skipping to next song: {e}')

def prev_song():
    """Skip to the previous track."""
    itunes = get_itunes_instance()
    if not itunes:
        return

    try:
        itunes.PreviousTrack()
        logging.info('Playing previous song.')
    except Exception as e:
        logging.error(f'Error skipping to previous song: {e}')

if __name__ == '__main__':
    play_pause_song()
