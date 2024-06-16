from pytube import YouTube
import os


## Documentation at https://code.pieces.app/blog/how-to-download-a-youtube-video-in-mp3-format-with-python


video = YouTube(str(input("Enter the URL of the video you want to download: \n")))

audio = video.streams.filter(only_audio = True).first()


print("Enter the destination (leave blank for current directory)")
destination = str(input(">>")) or '.'

out_file = audio.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(video.title + "has been successfully downloaded in .mp3 format")