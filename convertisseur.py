import pytube
from moviepy.editor import *
from unidecode import unidecode
import sqlite3
import pandas as pd

class VideoDownloader:
    def __init__(self):
        self.connection = sqlite3.connect('youtube_downloads.db')
        self.cursor = self.connection.cursor()
        self._create_database()

    def _create_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                size INTEGER,
                duration INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS music (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                size INTEGER,
                duration INTEGER
            )
        ''')
        self.connection.commit()

    def download_video(self, url):
        yt = pytube.YouTube(url)
        video = yt.streams.filter(file_extension='mp4').first()
        video.download()

        self.cursor.execute('''
            INSERT INTO videos (title, size, duration)
            VALUES (?, ?, ?)
        ''', (yt.title, video.filesize, yt.length))
        self.connection.commit()
        print("Video downloaded and information stored successfully!")

    def download_audio(self, url):
        yt = pytube.YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio_path = audio.download(filename='audio_temp')
    
        video = pytube.YouTube(url)
        video_title = video.title

        # Using unidecode to convert non-ASCII characters
        sanitized_title = unidecode(video_title)

        # Remove invalid characters for filename
        valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        sanitized_title = ''.join(c for c in sanitized_title if c in valid_chars)
        sanitized_title = sanitized_title.strip()[:100]  # Limiting to 100 characters for safety

        audio_clip = AudioFileClip(audio_path)
        audio_clip.write_audiofile(f"{sanitized_title}.mp3", codec='libmp3lame')
        audio_clip.close()

        # Store audio information in the database
        self.cursor.execute('''
            INSERT INTO music (title, size, duration)
            VALUES (?, ?, ?)
        ''', (sanitized_title, os.path.getsize(f"{sanitized_title}.mp3"), audio_clip.duration))
        self.connection.commit()
        print("Audio extracted and information stored as MP3!")

    def generate_excel_report(self):
        videos_df = pd.read_sql_query("SELECT * FROM videos", self.connection)
        music_df = pd.read_sql_query("SELECT * FROM music", self.connection)

        with pd.ExcelWriter('downloads_report.xlsx') as writer:
            videos_df.to_excel(writer, sheet_name='Videos', index=False)
            music_df.to_excel(writer, sheet_name='Music', index=False)

        print("Excel report generated successfully!")

    def close_connection(self):
        self.connection.close()


if __name__ == '__main__':

    youtube_url = input("Enter the YouTube URL: ")

    format_choice = input("Choose format (mp4 or mp3): ").lower()

    downloader = VideoDownloader()

    if format_choice == 'mp4':
        downloader.download_video(youtube_url)
        print("Video downloaded successfully!")
    elif format_choice == 'mp3':
        downloader.download_audio(youtube_url)
        print("Audio extracted and downloaded as MP3!")
    else:
        print("Invalid format choice. Please choose mp4 or mp3.")
        
    downloader.generate_excel_report()
    downloader.close_connection()