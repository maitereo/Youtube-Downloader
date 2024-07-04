#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: Yizhou Shan

# Description:
# This script is for downloading a YouTube video with just a link of the video page.

# Usage:
# 1. Run the script and it will ask you to paste the YouTube page link to the terminal
# 2. Hit enter to download the video
# 3. Wait until the complete message


from pytube import YouTube
import ffmpeg
import os

def main():

    # Format example
    # yt = YouTube(
    #         'https://www.youtube.com/watch?v=cpraXaw7dyc',
    #         on_progress_callback='progress_func',
    #         on_complete_callback='complete_func',
    #         proxies='my_proxies',
    #         use_oauth=False,
    #         allow_oauth_cache=True
    #     )

    # Examples of object definition 
    # yt = YouTube('https://www.youtube.com/watch?v=cpraXaw7dyc') # Optimus Gen 2
    # yt = YouTube('https://www.youtube.com/watch?v=1xChD-gv_pc') #Tesla Bot | Actuators Team
    # yt = YouTube('https://www.youtube.com/watch?v=D2vj0WcvH5c') # Tesla Bot Update | Sort & Stretch
    # yt = YouTube('https://www.youtube.com/watch?v=XiQkeWOFwmk=') # Tesla Bot Update
    # yt = YouTube('https://www.youtube.com/watch?v=f3d3blZGL20') # Toward Total Scene Understanding for Autonomous Driving—Drago Anguelov (Waymo)

    print("Enter the link of the YouTube video page\nEnter exit to quit.\n")
    usr_input_link = ''
    try:
        usr_input_link = str(input("Please enter: "))

    except ValueError:
        print("Sorry, invalid input value.")
        #better try again... Return to the start of the loop
        exit(1)
    
    else:
        if usr_input_link == 'exit':
            exit(0)

    yt = YouTube(usr_input_link)
    print("Title:\n" + yt.title + "\n")
    print("Thmbnail_url:\n" + yt.thumbnail_url + "\n")
    # List all resolution options and let the user pick
    print("Listing all resolutions of the video:")
    # for element in yt.streams.filter(mime_type='video/webm'):
    #     print(element)
    print(yt.streams.filter(mime_type='video/webm'))
    print("Enter the resolution you wish to download.\nExample: $ 2160p\nEnter exit to quit.\n")
    usr_input_video = ''
    try:
        usr_input_video = str(input("Please enter: "))

    except ValueError:
        print("Sorry, invalid input value.")
        #better try again... Return to the start of the loop
        exit(1)
    
    else:
        if usr_input_video == 'exit':
            exit(0)

    video_filename = ''
    try:
        print("Downloading video, please wait...")
        path = yt.streams.filter(resolution=usr_input_video).desc().first().download()
        filename = str.split(path,'/')[-1]
        video_filename = 'video_'+video_filename
        os.rename(filename, video_filename)
    except (ValueError, RuntimeError, TypeError, NameError):
        print("Video Download Failed, try again later.")
        
    audio_filename = ''
    try:
        print("Downloading audio, please wait...")
        path = yt.streams.filter(mime_type='audio/webm').desc().last().download()
        filename = str.split(path,'/')[-1]
        audio_filename = 'audio_'+audio_filename
        os.rename(filename, audio_filename)
    except (ValueError, RuntimeError, TypeError, NameError):
        print("Audio Download Faile, try again later")

    print("Downloaded")

    # To convert the webm to mp4 with H.264 encoding
    # ffmpeg -i input.webm  -c:v libx264 output.mp4
    # print("To convert the webm to mp4 with H.264 encoding, use:\nffmpeg -i input_video.webm -i input_audio.webm  -c:v libx264 -c:a aac output_combined.mp4")


    # <Stream: itag="313" mime_type="video/webm" res="2160p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    # [<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="12fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="313" mime_type="video/webm" res="2160p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="271" mime_type="video/webm" res="1440p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="avc1.640028" progressive="False" type="video">, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="244" mime_type="video/webm" res="480p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="24fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="24fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]




if __name__ == "__main__":
    main()
