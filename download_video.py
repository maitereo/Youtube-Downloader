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
import mergeav

def main():

    # Format example
    # yt = YouTube(
    #         url,
    #         on_progress_callback='progress_func',
    #         on_complete_callback='complete_func',
    #         proxies='my_proxies',
    #         use_oauth=False,
    #         allow_oauth_cache=True
    #     )

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
        video_filename = 'video_'+filename
        os.rename(filename, video_filename)
    except (ValueError, RuntimeError, TypeError, NameError):
        print("Video Download Failed, try again later.")
        
    audio_filename = ''
    try:
        print("Downloading audio, please wait...")
        path = yt.streams.filter(mime_type='audio/webm').desc().last().download()
        filename = str.split(path,'/')[-1]
        audio_filename = 'audio_'+filename
        os.rename(filename, audio_filename)
    except (ValueError, RuntimeError, TypeError, NameError):
        print("Audio Download Faile, try again later.")

    print(f"Downloaded /“{video_filename}/“ and /“{audio_filename}/“。")
    print(f"Merging /“{video_filename}/“ and /“{audio_filename}/“...")


    # To convert the webm to mp4 with H.264 encoding
    # ffmpeg -i input.webm  -c:v libx264 output.mp4
    # packed webm to mp4 conversion in mergeav

    mergeav.merge(video_file=video_filename, 
                  audio_file=audio_filename, 
                  output_file=yt.title+'.mp4')
    print("Merged。")

    os.remove(video_filename)
    os.remove(audio_filename)
    print(f"Removed /“{video_filename}/” and /“{audio_filename}/”。")

if __name__ == "__main__":
    main()
