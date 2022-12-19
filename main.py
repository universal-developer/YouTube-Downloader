import time
import os
from pytube import YouTube, Channel, Playlist
from colorama import Fore, Back, Style

DIR = str(input('Before we start, please, paste here a PATH to an your desktop directory: '))


def single_video(video_link): 
    yt = YouTube(f'{video_link}') #Initializing YouTube object
    video_title = yt.title #Setting a video title to get easier to use

    print(Fore.GREEN + f'Downloading: {video_title}\n------------------------')

    time.sleep(.3)

    print(Fore.YELLOW + 'Started working')

    os.chdir(f'{DIR}') #Going to the directory that you put there
        
    os.mkdir(f'{video_title}')  #Creating folder with name "Video title"

    os.chdir(f'{video_title}')  #Changing folder to video_title

    os.mkdir('video')  #Creating new folder: video_title/video

    os.chdir('video')  #Changing folder: video_title/video

    yt.streams.get_highest_resolution().download() #Downloading video in the highest resolution

    print(Fore.YELLOW + '1.Got video\n------------------------')

    time.sleep(.5)

    os.chdir('..')  #Changing directory to the previos one

    with open('thumbnail.txt', 'w') as f: #Opening file and writing the link on thumbnail
        f.write(yt.thumbnail_url) #Saving url of the thumbnail in file that was created rn
    print(Fore.YELLOW + '2.Got thumbnail\n------------------------') 

    time.sleep(.5)
    
    with open('title.txt', 'w') as f:  #Opening file and writing the name of the video
        f.write(video_title) #Writing title of the video in file that was created rn
    print(Fore.YELLOW + '3.Got title\n------------------------')

    time.sleep(.5)
    
    with open('description.txt', 'w') as f: #Opening file and writing there description of the video
        f.write(yt.description) #Writing description of the video in file that was created rn
    print(Fore.YELLOW + '4.Got description\n------------------------')

    time.sleep(.5)

    os.chdir('..')  # Changind directory to the previos one

    print(Fore.GREEN + 'Success')


def playlist(playlist_link):

    p = Playlist(f'{playlist_link}') #Initializing Playlist object

    print(Fore.GREEN + f'Downloading: {p.title}')

    os.chdir(f'{DIR}') #Going to the directory that you put there
    os.mkdir(f'{p.title}') # Creating folder with name "Video title"
    os.chdir(f'{p.title}') # Changing folder to Code/video_title

    for video in p.videos: #Running a loop to download each video from playlist (playlist.videos return a list of videos there)
        video_title = video.title #Setting a video title to get easier to use

        print(Fore.YELLOW+ f'Started working...\n------------------------')

        os.mkdir(f'{video_title}')  #Creating new folder: video_title

        os.chdir(f'{video_title}')  #Changing folder: video_title

        os.mkdir('video') #Creating folder 'video'

        os.chdir('video') #Changing folder to 'video'

        video.streams.get_highest_resolution().download() # Downloading video in the highest resolution

        os.chdir('..') #Changing directory to the previos one

        with open('thumbnail.txt', 'w') as f: #Opening file and writing the link on thumbnail
            f.write(video.thumbnail_url) #Saving url of the thumbnail in file that was created rn

        with open('title.txt', 'w') as f: #Opening file and writing the name of the video
            f.write(video_title) #Writing title of the video in file that was created rn

        with open('description.txt', 'w') as f: #Opening file and writing there description of the video
            f.write(video.description) #Writing description of the video in file that was created rn

        print(Fore.GREEN + f'Downloaded: {video_title}\n------------------------')

        os.chdir('..') #Changing directory to the previos one

        continue #keeping loop

    print(Fore.GREEN + 'Done')

def main(choice):
    if choice == 1:
        single_video(
            str(input('Paste here link on the video: '))
        )
    elif choice == 2:
        playlist(
            str(input('Paste here link on the playlist: '))
        )


main(
    int(input('Hi, dear user. Please choose a variant to use this script:\n1.Download single video\n2.Download whole playlist\\n\nYour choice: '))
)




