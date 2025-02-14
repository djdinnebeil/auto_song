import win32com.client

def get_current_itunes_song():
    try:
        itunes = win32com.client.Dispatch('iTunes.Application')
        current_track = itunes.CurrentTrack
        if current_track:
            return f'{current_track.Name} - {current_track.Artist}'
        else:
            return 'No song is currently playing'
    except Exception as e:
        return f'Error: {e}'

def next_song():
    try:
        itunes = win32com.client.Dispatch('iTunes.Application')
        itunes.NextTrack()
        print('Skipped to next song.')
    except Exception as e:
        print(f'Error: {e}')

def prev_song():
    try:
        itunes = win32com.client.Dispatch('iTunes.Application')
        itunes.PreviousTrack()
        print('Skipped to prev song.')
    except Exception as e:
        print(f'Error: {e}')

print(get_current_itunes_song())
next_song()
print(get_current_itunes_song())
prev_song()
print(get_current_itunes_song())