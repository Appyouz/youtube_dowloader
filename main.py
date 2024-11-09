from pytubefix import YouTube
from pytubefix.cli import on_progress


def video(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Downloading: {yt.title}")
    ys = yt.streams.get_highest_resolution()
    ys.download()
    print("Download complete.")



def main():
    # Prompt the user to enter a YouTube URL
    url = input("Please enter the YouTube URL to download: ")

    # Call the video function with the provided URL
    video(url)

if __name__ == "__main__":
    main()
