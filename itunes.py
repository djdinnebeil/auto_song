import win32com.client

def get_current_itunes_song():
    try:
        itunes = win32com.client.Dispatch("iTunes.Application")
        current_track = itunes.CurrentTrack
        if current_track:
            return f"{current_track.Name} - {current_track.Artist}"
        else:
            return "No song is currently playing"
    except Exception as e:
        return f"Error: {e}"

print(get_current_itunes_song())
